import { atom, read, update } from 'claude-code'
import type { EngineInterface, Register } from 'claude-code'

import { parseEstado } from './parse'

const estado = atom({ plugin: 'lumis-estado', key: 'estado' } as const, null)

// Relido no início da sessão (e a cada recarga do mod), ao fim de cada turno
// e a cada 30 s, para pegar também edições feitas fora do Claude.
const recarregar = async ($: EngineInterface) => {
  const md = await $.fs.read('ESTADO.md').catch(() => null)
  const novo = typeof md === 'string' ? parseEstado(md) : null
  await update($, estado, () => novo)
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    const result = await next(e)
    await recarregar($)
    $.clock.every(30_000, () => void recarregar($))

    return result
  })

  on('turn.complete', async ($, e, next) => {
    const result = await next(e)
    await recarregar($)

    return result
  })

  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    const atual = await read($, estado)
    if (e.props.hasSurvey || atual === null || atual.fase === null) return next(e)

    const { Box, Text } = $.ui.resolve(e)

    return (
      <Box flexDirection="column">
        <Box flexDirection="row" gap={1} key="fase">
          <Text bold color="cyan">
            LumisOS · {atual.fase}
          </Text>
          {atual.atualizadoEm !== null && (
            <Text dimColor>
              (ESTADO de {atual.atualizadoEm})
            </Text>
          )}
        </Box>
        {atual.andamento.map(item => (
          <Box flexDirection="row" key={item.codigo}>
            <Text color="yellow">● </Text>
            <Text wrap="truncate-end">
              {item.codigo} {item.nome}: {item.status}
            </Text>
          </Box>
        ))}
      </Box>
    )
  })
}
