import {readFile,writeFile,mkdir,readdir,copyFile,rm,stat} from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
const root=path.resolve(import.meta.dirname,'..'),site=path.join(root,'site'),dist=path.join(root,'dist');
await rm(dist,{recursive:true,force:true});await mkdir(path.join(dist,'assets'),{recursive:true});
const mapping=new Map();
async function walk(dir){let files=[];for(const e of await readdir(dir,{withFileTypes:true})){const p=path.join(dir,e.name);files.push(...(e.isDirectory()?await walk(p):[p]));}return files;}
for(const file of await walk(path.join(site,'assets'))){
 if(!/\.(webp|woff2|txt)$/i.test(file))continue;
 const bytes=await readFile(file),rel=path.relative(site,file).split(path.sep).join('/'),ext=path.extname(rel),hash=createHash('sha256').update(bytes).digest('hex').slice(0,12),dest=rel.slice(0,-ext.length)+'.'+hash+ext;
 await mkdir(path.dirname(path.join(dist,dest)),{recursive:true});await writeFile(path.join(dist,dest),bytes);mapping.set(rel,dest);
}
function refs(text){for(const [old,next]of mapping)text=text.replaceAll(old,next);return text;}
for(const name of ['style.css','script.js']){const bytes=Buffer.from(refs(await readFile(path.join(site,name),'utf8')));const h=createHash('sha256').update(bytes).digest('hex').slice(0,12);const dest=name.replace('.',`.${h}.`);await writeFile(path.join(dist,dest),bytes);mapping.set(name,dest);}
let html=refs(await readFile(path.join(site,'index.html'),'utf8'));
await writeFile(path.join(dist,'index.html'),html);
await writeFile(path.join(dist,'asset-manifest.json'),JSON.stringify(Object.fromEntries(mapping),null,2)+'\n');
const check=async()=>{const references=[...html.matchAll(/(?:src|href)="([^"]+)"/g)].map(x=>x[1]).filter(x=>!x.startsWith('#')&&!/^(https?:|mailto:|tel:|data:)/.test(x));for(const ref of references)await stat(path.join(dist,ref));const css=await readFile(path.join(dist,mapping.get('style.css')),'utf8');for(const ref of [...css.matchAll(/url\(['"]?([^'"\)]+)['"]?\)/g)].map(x=>x[1]))if(!/^(data:|https?:)/.test(ref))await stat(path.join(dist,ref));};
await check();console.log(`Site completo: ${mapping.size} arquivos versionados. Referências HTML e CSS verificadas.`);
