export type Andamento = { codigo: string; nome: string; status: string }

export type Estado = {
  fase: string | null
  atualizadoEm: string | null
  andamento: Andamento[]
}

declare module 'claude-code' {
  interface PluginState {
    'lumis-estado': { estado: Estado | null }
  }
}
