import type { On } from 'claude-code'
import type { Engine } from 'claude-code/testing'
import { expect, mock, test } from 'claude-code/testing'

import { parseEstado } from './parse'

const AMOSTRA = `# ESTADO — LumisOS

**Atualizado em:** 05/10/2026 · **Conferido contra:** arquivos reais.

## Onde estamos

**Fase 2 — O Mercado.** A F2-E1 está na v2.

## Entregas

| Código | Entrega | Arquivo vigente | Status |
|---|---|---|---|
| F1-E1 | Mapa da Situação | [PDF](x.pdf) | ✅ Revisada |
| F2-E1 | Mapa do Território | [**v2 .docx**](y.docx) | 🟡 v2 redigida; aguarda revisão da equipe |
| F2-E2 | Auditoria do Ativo | — | ⚪ A fazer |
| F2-A | Apêndice de Prompts | [Registro](z.md) | 🟡 Prompts registrados |

## Próximo passo

| F9-X | Fora da seção | — | 🟡 não deve entrar |
`

test('lê fase, data e só as entregas em andamento', async () => {
  expect(parseEstado(AMOSTRA)).toEqual({
    fase: 'Fase 2 — O Mercado',
    atualizadoEm: '05/10/2026',
    andamento: [
      { codigo: 'F2-E1', nome: 'Mapa do Território', status: 'v2 redigida; aguarda revisão da equipe' },
      { codigo: 'F2-A', nome: 'Apêndice de Prompts', status: 'Prompts registrados' },
    ],
  })
})

const BANDA = { hasSurvey: false, isWorking: false, maxRows: 10 } as never

const iniciar = async ($: Engine, on: On, fsRead: () => unknown) => {
  mock.clock(on)
  on('fs.read', fsRead as never)
  on('session.start', ($, e) => ({ cwd: e.cwd }))
  on('ui.render', ($, e) => {
    const { Box } = $.ui.resolve(e)

    return <Box key="vazio" />
  })
  await $.session.start({ cwd: '/lumis', surface: 'terminal', isInteractive: true })
}

test('desenha a faixa a partir do ESTADO.md', async ($, on) => {
  await iniciar($, on, () => ({ value: AMOSTRA }))

  for (const surface of ['terminal', 'desktop'] as const) {
    const ui = await $.ui.mount({ plugin: 'lumis-estado', surface, component: 'AbovePrompt', props: BANDA })
    const fase = (await ui.find({ key: 'fase' }))?.text
    expect(fase).toContain('LumisOS · Fase 2 — O Mercado')
    expect(fase).toContain('(ESTADO de 05/10/2026)')
    expect((await ui.find({ key: 'F2-A' }))?.text).toContain('F2-A Apêndice de Prompts: Prompts registrados')
    expect(await ui.find({ key: 'F2-E2' })).toBeUndefined()
  }
})

test('sem ESTADO.md, não desenha nada', async ($, on) => {
  await iniciar($, on, () => ({ deny: 'ENOENT' }))
  const ui = await $.ui.mount({ plugin: 'lumis-estado', surface: 'terminal', component: 'AbovePrompt', props: BANDA })
  expect(await ui.find({ key: 'fase' })).toBeUndefined()
})
