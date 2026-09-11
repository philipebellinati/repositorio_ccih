# tasks/todo.md

## Sessão 2026-09-10 — Projeto de pesquisa: app de antibioticoterapia empírica (HEL + HCL)

Contexto: o usuário pediu a estrutura do projeto de pesquisa (justificativa, base de
conhecimento, passo a passo metodológico) para o app de antibioticoterapia empírica
parametrizado pela epidemiologia local de dois hospitais, com medida de conformidade
antes-depois. Deliverable: documento em `docs/` + resumo no chat. Sem alteração de código.

### Plano
- [x] 1. Levantar referências verificáveis (2 subagentes: evidência clínica/AMS; métodos)
- [x] 2. Calcular tabela de tamanho amostral para cenários plausíveis de conformidade
- [x] 3. Escrever `docs/projeto_pesquisa_app_antibioticoterapia.md` com:
  - [x] identificação, resumo, introdução e justificativa
  - [x] hipóteses e objetivos
  - [x] base de conhecimento (tópicos da fundamentação teórica, com o que dizer em cada um)
  - [x] método passo a passo (antibiograma → Delphi → app → implantação/UX → conformidade)
  - [x] variáveis, desfechos, amostra, análise
  - [x] riscos, ética, LGPD, cronograma, orçamento, produtos, limitações
  - [x] anexos: instrumento de auditoria de conformidade, roteiro Delphi, itens SUS
- [x] 4. Integrar referências verificadas (com PMID/DOI) e marcar as não verificadas
- [x] 5. Revisar o documento (consistência interna, sem números inventados) 
- [x] 6. Commit + push no branch `claude/antibiotic-prophylaxis-therapy-research-c3zya9`

### Revisão (2026-09-11)
- Entregue `docs/projeto_pesquisa_app_antibioticoterapia.md` (655 linhas): 20 seções + 7 anexos.
- 80 referências, 63 com PMID/DOI conferidos no PubMed; 17 documentos normativos só por busca web
  (gov.br/planalto bloqueados no ambiente); nada inventado, títulos não confirmados ficaram entre colchetes.
- Achados que mudaram o desenho: (1) não existe versão brasileira validada do MAUQ, então SUS-BR
  (Lourenço 2022) é o instrumento principal; (2) o P&R da ANVISA sobre a RDC 657/2022 enquadra calculadora
  de dose e apoio à decisão por protocolo como SaMD, então o projeto precisa documentar o enquadramento e
  pedir posicionamento formal; (3) a exportação do laboratório do HCL não tem identificador de paciente,
  exigido pela regra do primeiro isolado (CLSI M39).
- 22 marcadores [DADO LOCAL] e 15 [DECIDIR] com recomendação registrada (seção 19).
- Tabela de tamanho amostral calculada (duas proporções, alfa 5%, poder 80% e 90%).
- Sem alteração de código; branch `claude/antibiotic-prophylaxis-therapy-research-c3zya9`.

