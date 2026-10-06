import type { Andamento, Estado } from '../types'

const limpar = (texto: string) =>
  texto
    .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')
    .replace(/\*\*/g, '')
    .replace(/🟡/g, '')
    .trim()

const secao = (md: string, titulo: string) => {
  const inicio = md.indexOf(`## ${titulo}`)
  if (inicio === -1) return ''
  const resto = md.slice(inicio + titulo.length + 3)
  const fim = resto.search(/^## /m)

  return fim === -1 ? resto : resto.slice(0, fim)
}

// Lê o ESTADO.md: a fase de "Onde estamos" e as linhas 🟡 da tabela de Entregas.
export const parseEstado = (md: string): Estado => {
  const fase = secao(md, 'Onde estamos').match(/\*\*(Fase[^*]*?)\.?\*\*/)?.[1] ?? null
  const atualizadoEm = md.match(/\*\*Atualizado em:\*\*\s*([0-9/]+)/)?.[1] ?? null

  const andamento: Andamento[] = secao(md, 'Entregas')
    .split('\n')
    .filter(linha => linha.startsWith('|'))
    .map(linha => linha.split('|').slice(1, -1).map(c => c.trim()))
    .flatMap(celulas => {
      const [codigo = '', nome = ''] = celulas
      const status = celulas.at(-1) ?? ''

      return celulas.length >= 2 && status.startsWith('🟡')
        ? [{ codigo: limpar(codigo), nome: limpar(nome), status: limpar(status) }]
        : []
    })

  return { fase, atualizadoEm, andamento }
}
