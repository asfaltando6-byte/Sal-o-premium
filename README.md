# Catálogo Salão Premium

Site completo com imagens locais, Montserrat, carrossel automático, amostras ampliáveis, bônus exclusivos do Premium, garantia de 7 dias e os dois checkouts Cakto.

## Publicar na Vercel

Importe este repositório na Vercel. A configuração já está em `vercel.json`:

- Framework: **Other**
- Root Directory: raiz do repositório
- Build Command: `npm run build`
- Output Directory: `dist`
- Node.js: **22.x**

Não exige variáveis de ambiente, banco de dados nem serviços de imagem externos. O build usa apenas APIs nativas do Node.js, sem dependências npm.

## Desenvolvimento

```bash
npm run build
npm run dev
```

Abra `http://localhost:3000`. O comando `npm run dev` serve o último build.

## Onde editar

- `site/index.html`: conteúdo e estrutura.
- `site/style.css`: estilos otimizados.
- `site/script.js`: checkouts, carrossel e ampliação.
- `site/assets/`: imagens e fontes.
- `source/originais/`: HTML, CSS e JavaScript originais legíveis, antes da otimização.
- `source/build-catalog.py`: fonte das páginas demonstrativas do carrossel.
- `dist/`: versão publicada, regenerada por `npm run build`.

Depois de qualquer alteração em `site/`, execute `npm run build`. O build gera nomes com hash para evitar arquivos antigos no cache.

## Links de pagamento

- Essencial R$ 9,90: https://pay.cakto.com.br/tghh3wc_1304857
- Premium R$ 27,00: https://pay.cakto.com.br/iamnr2b

## Otimizações preservando o visual

Fontes WOFF2 locais com caracteres em português, preload dos pesos usados na primeira tela, preload do mockup principal, JavaScript adiado, decodificação assíncrona e carregamento sob demanda das imagens abaixo da primeira tela, CSS/JS minificados e arquivos versionados com cache de longa duração.

As imagens WebP originais foram preservadas sem recompactação, recorte ou mudança de cores. As versões originais PNG e TTF ficam no código-fonte para manutenção. Os arquivos comerciais do kit não fazem parte desta página pública.

## Fontes e imagens

Montserrat é distribuída sob SIL Open Font License. Veja `site/assets/fonts/OFL.txt`. As fotos e os mockups deste projeto foram criados para esta página. As páginas do carrossel são modelos para personalização.
