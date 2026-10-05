# Gabriela Bueno Hair Colorist

Landing page de uma página para a Gabriela Bueno, hair colorist em Maringá PR (mechas, mega hair, correção de cor, cursos). Site estático (HTML, CSS e JavaScript puros), sem build, sem dependências em tempo de execução. Abra `index.html` ou sirva a pasta com qualquer servidor estático (`python3 -m http.server 4196`).

## Dados do cliente

| Campo | Valor |
| --- | --- |
| Nome | Gabriela Bueno (no Google: Gabriela Bueno Hair Colorist) |
| Segmento | Hair colorist: mechas e mega hair |
| Público | Homens e mulheres |
| WhatsApp | (44) 99177-5276, `https://wa.me/5544991775276` |
| Instagram | [@gabrielahbueno](https://www.instagram.com/gabrielahbueno/) |
| Endereço | R. Ten. Afonso Pinheiro Camargo, 23, Sala 01, Vila Progresso, Maringá PR, CEP 87080-016 |
| Horário | Segunda a quinta 9h às 19h; sexta e sábado 9h às 20h; domingo fechado |
| Nota no Google | 5,0 (5 avaliações em 05/10/2026) |
| Frases do briefing | "Mechas e mega hair", "Há 8 anos atuando na área da beleza", "Posso transformar sua autoestima", "Agendamentos para atendimentos e cursos" |
| Do Instagram | "O trabalho que eu mais tenho feito ultimamente no salão, correção de cor e devolução de fundo. Todas em busca de naturalidade e de menos manutenções." |
| Telefone fixo, e-mail, preços | Não informados |

### Conferido no Google (05/10/2026)

Busca "Gabriela Bueno Hair Colorist, R. Ten. Afonso Pinheiro Camargo, 23, Maringá" no Maps: ficha **Gabriela Bueno Hair Colorist**, endereço igual ao briefing com CEP 87080-016, **5,0 em 5 avaliações**. Bate com o briefing; a página cita "Nota 5 no Google" (sem a quantidade, que é pequena) e o `aggregateRating` dos dados estruturados traz o 5 de 5. O mapa carrega pelo nome e endereço.

### Avaliações (texto original)

- **Calliê Maiana:** "A melhor de todas , principalmente em tratamento pós mechas! Super indico de olhos fechados"
- **Ana Paula:** "Excelente profissional. Nunca tinha pintado meu cabelo antes e deixei nas mãos dela para realizar esse sonho e ficou melhor do que eu imaginava ."
- **Natália Kosinski:** "Sou atendida pela gab à 03 anos e onde ela vai eu vou hahaha Agora com o salão dela o atendimento está ainda melhor e o salão está incrível!! Super indico!!"

Na página, só pontuação e espaços foram ajustados ("pela Gab há 03 anos", vírgulas, pontos finais). O conteúdo é o mesmo. Não vieram fotos de perfil; aparece só o nome.

## Síntese estratégica

| Definição | Decisão |
| --- | --- |
| Proposta de valor | Cor com cara de natural e menos manutenção: mechas, mega hair e correção de cor por uma colorista com 8 anos de área e salão próprio |
| Principal objeção | "Vai ficar artificial, vai estragar meu cabelo ou vou ter que retocar toda hora" |
| Conversão prioritária | Agendar pelo WhatsApp (mensagens por assunto: horário, avaliação, cursos) |
| Direção visual | Editorial de beleza com as cores do próprio salão (marfim, taupe, dourado do monograma, marrom profundo); Bodoni Moda + Jost |

## Direção visual

- **Cores**: dourado `#a07127` medido no monograma (molduras, estrelas, detalhes; `#7a5416` para texto sobre claro, AA), marfim `#f7f3ed` e taupe das paredes e poltronas do salão, marrom profundo `#2b2420` para cabeçalho, seção do salão, fecho e rodapé, `#ecd6b0` para o monograma e destaques sobre o marrom.
- **Fontes**: **Bodoni Moda** nos títulos (serifa de alto contraste, como capa de revista; itálico para a segunda parte dos títulos) e **Jost** no texto e nos rótulos em caixa alta espaçada (geométrica, como o "GABRIELA BUENO HAIR COLORIST" do logo). Arquivos locais em `assets/fonts`, subconjunto latino.
- **Composição**: hero como **página dupla de revista**: título atravessa a largura toda e, embaixo, texto à esquerda com duas fotos em molduras douradas finas, a segunda deslocada para baixo. Molduras de filete dourado em todas as fotos. Nada de sombra, degradê ou efeito de vidro.
- **Logo**: o monograma veio sobre branco (1254 px); o script separa o traço do fundo pela luminosidade e gera versões dourada e clara com transparência, usadas no cabeçalho (ao lado do nome em Bodoni), no fecho, no rodapé e nos ícones. O nome por extenso não veio como imagem, por isso é texto.

## Estrutura

Cabeçalho → Hero (página dupla) → Serviços (lista numerada: mechas e loiros, correção de cor e devolução de fundo, mega hair, cuidado pós-mechas; citação da Gabriela ao lado do título; nota sobre cursos) → Trabalhos (galeria de 5 fotos com legendas) → O salão (foto, horário, como marcar, produtos Joico K-Pak) → Avaliações (3) → Como agendar (3 passos) → Onde fica (contatos, horário em tabela, mapa) → Fecho → Rodapé. Botão flutuante de WhatsApp em todas as telas.

## Imagens

Todas vêm de `materiais-de-origem/` e são geradas por `tools/optimize-images.py` (Pillow). Nenhuma é ampliada.

| Arquivo em `assets/img` | Origem | Uso | Observação |
| --- | --- | --- | --- |
| `loiro-ondulado-*` | `Screenshot ... 142946.png` (715x892) | Hero (foto A) e compartilhamento | Seta do carrossel e pontos do Instagram cortados (borda direita e base) |
| `loiro-mel-*` | `Screenshot ... 143022.png` | Hero (foto B) e compartilhamento | idem |
| `loiro-longo-*` | `Screenshot ... 143002.png` | Trabalhos | idem |
| `morena-iluminada-*` | `Screenshot ... 143038.png` | Trabalhos | idem |
| `loiro-curto-*` | `Screenshot ... 143228.png` (562x750) | Trabalhos | Menor; exibida em até 380 px |
| `costas-mel-*`, `costas-castanho-*` | `imagem-03.png`, `imagem-04.png` (1099x1431) | Trabalhos | |
| `salao-*` | `imagem-01.png` (1464x1074) | O salão | |
| `produtos-*` | `imagem-02.png` (1098x1433) | O salão (miniatura) | Linha Joico K-Pak; base para a frase sobre cuidado pós-mechas |
| `monograma-*`, `monograma-claro-*` | `logo/Logo.png` | Cabeçalho, fecho, rodapé | Gerados com transparência |
| `favicon-32`, `apple-touch-icon`, `icon-192` | monograma sobre marfim | Ícones | `optimize-images.py` |
| `compartilhamento.jpg` | montagem 1200x630 | Open Graph / WhatsApp | `node tools/render-compartilhamento.js` |

`imagem-05.png` (o monograma em relevo sobre uma parede) é uma imagem gerada por IA, não uma foto do salão: **não é usada**. Um arquivo `ChatGPT Image ...:Zone.Identifier` vazio veio junto e foi descartado.

## Links e mensagens

| Onde | Destino |
| --- | --- |
| Agendar (cabeçalho, hero, contatos, fecho, rodapé, botão flutuante) | WhatsApp: "Olá, Gabriela! Vi o site e quero agendar um horário." |
| Pedir uma avaliação (Serviços) | WhatsApp: "Olá, Gabriela! Vi o site e quero uma avaliação para mechas ou mega hair." |
| cursos (Serviços) | WhatsApp: "Olá, Gabriela! Vi o site e quero informações sobre os cursos." |
| Instagram | https://www.instagram.com/gabrielahbueno/ |
| Endereço, Abrir no Google Maps, Como chegar | `https://www.google.com/maps/search/?api=1&query=Gabriela+Bueno+Hair+Colorist, R. Ten. Afonso Pinheiro Camargo, 23, Maringá PR` |

## Decisões

- Os quatro serviços vêm do briefing (mechas, mega hair), do Instagram (correção de cor e devolução de fundo, "o que mais tenho feito") e da avaliação da Calliê + foto dos produtos (cuidado pós-mechas com Joico K-Pak). Nenhuma técnica, prazo ou preço foi inventado.
- "Salão próprio" e "agora com o salão dela" vêm da avaliação da Natália e do endereço com sala; "8 anos" vem do briefing.
- Cursos aparecem como nota com link, sem datas nem conteúdo (não informados).
- Texto marrom sobre o botão dourado claro (o branco não atinge contraste AA sobre dourado).
- Sem JS tudo aparece, menu fica aberto e o botão de menu some.

## Testes (05/10/2026, Chromium via Playwright)

41 verificações aprovadas: sem rolagem horizontal de 320 a 1920 px; título do hero em 2 linhas no desktop e 3 no celular; contraste AA em todos os textos; menu no celular (abre, Esc fecha, foco volta, toques ≥ 48 px); teclado e link de pular; sem JS; movimento reduzido; carga inicial no celular abaixo de 700 KB (763 KB a página inteira, mais o mapa só ao chegar na seção); nenhuma imagem exibida acima do tamanho original em 390 e 1920 px; dados estruturados `HairSalon` com endereço, horários e `aggregateRating`.

## Pendências

- Fotos de perfil das avaliações, se autorizadas.
- Datas e conteúdo dos cursos, se a Gabriela quiser publicar.
- Publicar e apontar o domínio; trocar `og:image` por URL absoluta quando houver domínio.

## Estrutura de arquivos

```
index.html
assets/css/styles.css
assets/js/main.js
assets/fonts/      Bodoni Moda e Jost (woff2, subconjunto latino)
assets/img/        imagens otimizadas (geradas)
tools/optimize-images.py
tools/render-compartilhamento.js
materiais-de-origem/   originais do cliente (fora do git)
```
