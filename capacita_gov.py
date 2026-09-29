# CAPACITA GOV - protótipo (execute este arquivo em um Python online)
# Sobe um servidor local e abre o site. Em Replit/OnlineGDB, use a aba/porta "Webview".
import http.server, socketserver, threading, webbrowser, os

PORT = int(os.environ.get("PORT", 8000))

HTML = r'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>CAPACITA GOV</title>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;800&display=swap" rel="stylesheet">
<style>
:root{--bg:#070d1c;--bg2:#0d1630;--card:#111b38;--line:#1f2c52;--tx:#e8eeff;--mu:#8e9bc4;--g:#5ef2b0;--gd:#0a2a20;--p:#8b5cf6;--r:18px;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
:root[data-theme=light]{}
*{box-sizing:border-box}html{scroll-padding-top:env(safe-area-inset-top,0px)}
body{margin:0;background:var(--bg);color:var(--tx);font:400 15px/1.5 Manrope,system-ui,-apple-system,Segoe UI,sans-serif}
button,select,input{font:inherit;color:inherit}
button{cursor:pointer}
:focus-visible{outline:2px solid var(--g);outline-offset:2px}
#side{position:fixed;inset:0 auto 0 0;width:250px;background:var(--bg2);border-right:1px solid var(--line);padding:22px 14px;display:flex;flex-direction:column;gap:4px;z-index:20;overflow-y:auto;transition:transform .2s}
.logo{font-weight:800;font-size:20px;letter-spacing:.5px;padding:0 10px 4px}.logo b{color:var(--g)}
.slog{color:var(--mu);font-size:12px;padding:0 10px 18px}
.nav{background:none;border:0;text-align:left;padding:10px 12px;border-radius:12px;color:var(--mu);font-weight:600;display:flex;gap:10px;align-items:center}
.nav:hover{background:var(--card);color:var(--tx)}
.nav.on{background:var(--gd);color:var(--g);box-shadow:inset 3px 0 0 var(--g)}
.user{margin-top:auto;display:flex;gap:10px;align-items:center;padding:12px;background:var(--card);border-radius:14px}
.av{width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,var(--p),var(--g));display:grid;place-items:center;font-weight:800;color:#06101f;flex:none}
main{margin-left:250px;padding:28px 32px 60px;max-width:1200px}
#menu{display:none;position:fixed;top:10px;left:10px;z-index:30;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:8px 12px}
h1{font-size:28px;margin:0 0 4px;font-weight:800}h2{font-size:19px;margin:30px 0 14px}h3{margin:0;font-size:16px}
.mu{color:var(--mu)}.sm{font-size:13px}
.note{background:#1b1740;border:1px solid #3a2f7a;color:#cfc4ff;border-radius:12px;padding:10px 14px;font-size:13px;margin:14px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:20px}
.hero{display:grid;grid-template-columns:1.6fr 1fr;gap:18px;margin-top:20px}
.hero .main{background:linear-gradient(135deg,#123a3a,#221a52);border-color:#2b3f7a}
.bar{height:10px;background:#0a1226;border-radius:9px;overflow:hidden;margin:10px 0}
.bar i{display:block;height:100%;background:linear-gradient(90deg,var(--g),var(--p));border-radius:9px;transition:width .4s}
.btn{background:var(--g);color:#04170f;border:0;border-radius:12px;padding:10px 18px;font-weight:800}
.btn:hover{filter:brightness(1.1)}
.btn.o{background:none;color:var(--g);border:1px solid var(--g)}
.btn.p{background:var(--p);color:#fff}
.btn:disabled{opacity:.45;cursor:default}
.stats{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:10px}
.stat b{font-size:26px;display:block;color:var(--g)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}
.cc{display:flex;flex-direction:column;gap:10px}
.cc h3{min-height:42px}
.tags{display:flex;flex-wrap:wrap;gap:6px}
.tag{font-size:12px;border-radius:99px;padding:3px 10px;background:#0a1226;border:1px solid var(--line);color:var(--mu)}
.tag.g{color:var(--g);border-color:#1d6b4d}.tag.p{color:#c4b0ff;border-color:#4b3a95}
.row{display:flex;gap:10px;align-items:center;flex-wrap:wrap}.sp{margin-left:auto}
.fav{background:none;border:0;font-size:20px;line-height:1}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin:14px 0}
.chip{background:var(--card);border:1px solid var(--line);border-radius:99px;padding:7px 14px;font-weight:600;color:var(--mu)}
.chip.on{background:var(--gd);border-color:var(--g);color:var(--g)}
.filters{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;align-items:end}
.filters label{font-size:12px;color:var(--mu);display:flex;flex-direction:column;gap:4px}
select,input[type=search],input[type=text]{background:#0a1226;border:1px solid var(--line);border-radius:10px;padding:9px 10px;width:100%}
.ck{flex-direction:row!important;align-items:center;gap:8px!important;font-size:14px!important;color:var(--tx)!important}
.mod{display:flex;gap:12px;align-items:center;padding:12px 14px;border:1px solid var(--line);border-radius:14px;margin-bottom:8px;background:#0d1631}
.mod.done{border-color:#1d6b4d}.mod .ck2{width:26px;height:26px;border-radius:50%;border:2px solid var(--line);display:grid;place-items:center;flex:none;color:#04170f;font-weight:800}
.mod.done .ck2{background:var(--g);border-color:var(--g)}
.two{display:grid;grid-template-columns:1.5fr 1fr;gap:18px;margin-top:18px}
.win{background:linear-gradient(135deg,#0f3a2c,#2a1c63);border:1px solid var(--g);border-radius:var(--r);padding:18px;margin-bottom:16px}
#toast{position:fixed;bottom:22px;right:22px;background:var(--g);color:#04170f;font-weight:800;padding:12px 18px;border-radius:12px;opacity:0;transform:translateY(10px);transition:.25s;pointer-events:none;z-index:60}
#toast.on{opacity:1;transform:none}
#modal{position:fixed;inset:0;background:rgba(3,6,15,.8);display:none;place-items:center;z-index:50;padding:16px;overflow:auto}
#modal.on{display:grid}
.cert{background:#f6f3e8;color:#1a1a2e;border:8px double #7c5cd6;border-radius:6px;padding:34px 26px;max-width:640px;text-align:center;font-family:Georgia,"Times New Roman",serif}
.cert h2{margin:8px 0;font-size:28px}.cert .nm{font-size:30px;margin:12px 0;color:#5b3fc2}
.dash{display:flex;align-items:center;gap:10px;margin:8px 0}.dash span{width:150px;font-size:13px}.dash .bar{flex:1;margin:0}
@media(max-width:860px){#side{transform:translateX(-100%)}#side.on{transform:none}#menu{display:block}main{margin-left:0;padding:60px 16px 50px}.hero,.two{grid-template-columns:1fr}h1{font-size:23px}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
</head>
<body>
<button id="menu" onclick="document.getElementById('side').classList.toggle('on')" aria-label="Abrir menu">☰ Menu</button>
<aside id="side"></aside>
<main id="app"></main>
<div id="modal" onclick="if(event.target===this)closeM()"></div>
<div id="toast" role="status"></div>
<script>
const C=[
{id:1,t:'Introdução à Administração Pública',i:'Escola de Governo',h:20,l:'Básico',a:'Administração Pública',m:'EaD',d:'Visão geral do funcionamento do Estado e da gestão pública.',mods:'O Estado e a administração|Princípios da gestão pública|Servidores e carreiras|Controle e transparência'},
{id:2,t:'Gestão de Projetos no Setor Público',i:'Escola Nacional de Administração Pública',h:30,l:'Intermediário',a:'Gestão de Projetos',m:'EaD',d:'Planejamento, execução e monitoramento de projetos em órgãos públicos.',mods:'Iniciação do projeto|Planejamento|Execução e riscos|Monitoramento|Encerramento'},
{id:3,t:'Governo Digital',i:'Órgão Público',h:25,l:'Básico',a:'Governo Digital',m:'Autoinstrucional',d:'Serviços digitais, dados abertos e transformação digital no governo.',mods:'O que é governo digital|Serviços centrados no cidadão|Dados abertos|Cultura digital'},
{id:4,t:'Segurança da Informação',i:'Instituição Pública',h:40,l:'Intermediário',a:'Segurança da Informação',m:'EaD',d:'Boas práticas de proteção de dados e sistemas no serviço público.',mods:'Conceitos básicos|Ameaças e riscos|Controles e políticas|LGPD no setor público|Resposta a incidentes'},
{id:5,t:'Excel para Administração Pública',i:'Escola de Governo',h:20,l:'Básico',a:'Tecnologia',m:'Autoinstrucional',d:'Planilhas aplicadas a rotinas administrativas e relatórios.',mods:'Fundamentos|Fórmulas essenciais|Tabelas e gráficos|Relatórios'},
{id:6,t:'Ética no Serviço Público',i:'Escola de Governo',h:15,l:'Básico',a:'Administração Pública',m:'EaD',d:'Princípios éticos, conduta e responsabilidade do agente público.',mods:'Ética e moralidade|Conduta do servidor|Conflito de interesses'},
{id:7,t:'Noções de Direito Administrativo',i:'Universidade Pública',h:30,l:'Intermediário',a:'Direito',m:'Híbrido',d:'Atos, contratos e princípios do direito administrativo.',mods:'Princípios|Atos administrativos|Licitações e contratos|Responsabilidade'},
{id:8,t:'Orçamento Público',i:'Órgão Público',h:25,l:'Intermediário',a:'Finanças Públicas',m:'EaD',d:'Ciclo orçamentário, receitas e despesas públicas.',mods:'Ciclo orçamentário|Receitas|Despesas|Execução e controle'},
{id:9,t:'Liderança e Gestão de Pessoas',i:'Instituto Federal',h:20,l:'Básico',a:'Gestão de Pessoas',m:'Híbrido',d:'Liderança, comunicação e desenvolvimento de equipes.',mods:'Liderança|Comunicação|Feedback e equipes'}];
const CATS=[['💻','Tecnologia'],['🏛️','Administração Pública'],['📊','Gestão'],['⚖️','Direito'],['💰','Finanças Públicas'],['🔐','Segurança da Informação'],['📈','Gestão de Projetos'],['🌐','Governo Digital'],['👥','Gestão de Pessoas']];
const INST=[['Escolas de Governo','Formação continuada de servidores e gestores.','Escola de Governo'],['Escola Nacional de Administração Pública','Exemplo de escola nacional de governo.','Escola Nacional de Administração Pública'],['Ministérios','Órgãos do Poder Executivo federal.',null],['Institutos Federais','Educação profissional e tecnológica pública.','Instituto Federal'],['Universidades Públicas','Ensino, pesquisa e extensão gratuitos.','Universidade Pública'],['Órgãos públicos','Autarquias, agências e secretarias.','Órgão Público'],['Instituições públicas','Demais entidades da administração pública.','Instituição Pública']];
const S={v:'home',cid:null,en:{1:2,6:3},fav:new Set([3]),done:{6:'10/09/2026'},name:'Marco',f:{q:'',a:'',i:'',h:'',l:'',m:'',free:false,cert:false}};
const $=id=>document.getElementById(id);
const byId=id=>C.find(c=>c.id===id);
const ML=c=>c.mods.split('|');
const isEn=c=>c.id in S.en;
const isDone=c=>isEn(c)&&S.en[c.id]>=ML(c).length;
const pct=c=>isEn(c)?Math.round(S.en[c.id]/ML(c).length*100):0;
const hrs=()=>C.reduce((s,c)=>s+(isEn(c)?S.en[c.id]*c.h/ML(c).length:0),0);
const fmt=n=>(Math.round(n*10)/10).toString().replace('.',',');
const code=c=>'CG-DEMO-'+(1000+c.id*137);
const NAV=[['home','🏠','Início'],['cursos','📚','Cursos'],['explorar','🔎','Explorar cursos'],['progresso','📈','Meu progresso'],['certs','🏆','Certificados'],['favs','⭐','Favoritos'],['inst','🏛️','Instituições'],['desempenho','📊','Meu desempenho'],['perfil','👤','Perfil']];
function toast(m){const t=$('toast');t.textContent=m;t.classList.add('on');clearTimeout(toast.h);toast.h=setTimeout(()=>t.classList.remove('on'),2200)}
function go(v,keep){S.v=v;if(!keep)S.cid=null;$('side').classList.remove('on');render();scrollTo(0,0)}
function openC(id){S.v='curso';S.cid=id;$('side').classList.remove('on');render();scrollTo(0,0)}
function enroll(id){S.en[id]=0;toast('Inscrição realizada!');render()}
function complete(id){const c=byId(id);S.en[id]++;const fin=isDone(c);if(fin)S.done[id]=new Date().toLocaleDateString('pt-BR');toast(fin?'Curso concluído! 🎉':'Módulo concluído ✔');render()}
function fav(id){S.fav.has(id)?S.fav.delete(id):S.fav.add(id);render()}
function setF(k,v){S.f[k]=v;if(S.v==='home'||S.v==='cursos')S.v='explorar';render()}
function clearF(){S.f={q:'',a:'',i:'',h:'',l:'',m:'',free:false,cert:false};render()}
function showCert(id){const c=byId(id);$('modal').innerHTML=`<div><div class="cert"><div>🏛️ CAPACITA GOV</div><h2>Certificado de Conclusão</h2><div>Certificamos que</div><div class="nm">${S.name}</div><div>concluiu o curso <b>${c.t}</b><br>${c.i} · ${c.h} horas</div><p>Concluído em ${S.done[id]}<br>Código: <b>${code(c)}</b></p><p style="font-size:12px;color:#666">Certificado demonstrativo. Sem valor oficial.</p></div><div class="row" style="justify-content:center;margin-top:12px"><button class="btn" onclick="print()">Imprimir</button><button class="btn o" onclick="closeM()">Fechar</button></div></div>`;$('modal').classList.add('on')}
function closeM(){$('modal').classList.remove('on')}
function greet(){const h=new Date().getHours();return h<12?'Bom dia':h<18?'Boa tarde':'Boa noite'}
function card(c){const p=pct(c);return `<article class="card cc"><div class="row"><div class="tags"><span class="tag g">Gratuito</span><span class="tag p">Curso demonstrativo</span></div><button class="fav sp" onclick="fav(${c.id})" aria-label="Favoritar">${S.fav.has(c.id)?'⭐':'☆'}</button></div><h3>${c.t}</h3><div class="mu sm">${c.i}</div><div class="tags"><span class="tag">${c.h} horas</span><span class="tag">${c.l}</span><span class="tag">${c.m}</span></div>${isEn(c)?`<div class="bar"><i style="width:${p}%"></i></div><div class="sm mu">${p}% concluído</div>`:''}<button class="btn sp0" style="margin-top:auto" onclick="openC(${c.id})">${isEn(c)?'Continuar curso':'Ver curso'}</button></article>`}
function inProg(){return C.filter(c=>isEn(c)&&!isDone(c))}
function vHome(){const cur=inProg()[0];const done=C.filter(isDone).length;
let hero=cur?`<div class="card main"><div class="sm mu">Continue sua capacitação</div><h2 style="margin:6px 0">${cur.t}</h2><div class="mu sm">${cur.i} · Curso demonstrativo</div><div class="bar"><i style="width:${pct(cur)}%"></i></div><div class="row sm"><b>${pct(cur)}% concluído</b><span class="mu">${S.en[cur.id]} de ${ML(cur).length} módulos</span><span class="mu">${fmt((ML(cur).length-S.en[cur.id])*cur.h/ML(cur).length)} h restantes</span></div><button class="btn" style="margin-top:14px" onclick="openC(${cur.id})">Continuar curso</button></div>`:`<div class="card main"><div class="sm mu">Continue sua capacitação</div><h2>Nenhum curso em andamento</h2><p class="mu">Escolha um curso gratuito para começar.</p><button class="btn" onclick="go('explorar')">Explorar cursos</button></div>`;
return `<h1>${greet()}, ${S.name} 👋</h1><div class="mu">Capacitação pública para transformar resultados.</div><div class="note">Protótipo: os cursos e instituições abaixo são exemplos demonstrativos e não representam ofertas reais.</div>
<div class="hero">${hero}<div class="card"><h3>Seu progresso</h3><div class="stats"><div class="stat"><b>${done}</b><span class="sm mu">Cursos concluídos</span></div><div class="stat"><b>${inProg().length}</b><span class="sm mu">Em andamento</span></div><div class="stat"><b>${done}</b><span class="sm mu">Certificados</span></div><div class="stat"><b>${fmt(hrs())}</b><span class="sm mu">Horas estudadas</span></div></div></div></div>
<h2>Categorias</h2><div class="chips">${CATS.map(c=>`<button class="chip" onclick="setF('a','${c[1]}')">${c[0]} ${c[1]}</button>`).join('')}</div>
<h2>Cursos em destaque</h2><div class="grid">${C.slice(0,6).map(card).join('')}</div>`}
function filtered(){const f=S.f;return C.filter(c=>(!f.q||(c.t+c.i).toLowerCase().includes(f.q.toLowerCase()))&&(!f.a||c.a===f.a)&&(!f.i||c.i===f.i)&&(!f.l||c.l===f.l)&&(!f.m||c.m===f.m)&&(!f.h||(f.h==='1'?c.h<=20:f.h==='2'?c.h>20&&c.h<=30:c.h>30)))}
function sel(k,lab,opts){return `<label>${lab}<select onchange="setF('${k}',this.value)"><option value="">Todos</option>${opts.map(o=>Array.isArray(o)?`<option value="${o[0]}" ${S.f[k]===o[0]?'selected':''}>${o[1]}</option>`:`<option ${S.f[k]===o?'selected':''}>${o}</option>`).join('')}</select></label>`}
function vExplorar(){const r=filtered();const f=S.f;
return `<h1>Explorar cursos</h1><div class="mu">Cursos demonstrativos gratuitos de capacitação pública.</div>
<div class="chips">${CATS.map(c=>`<button class="chip ${f.a===c[1]?'on':''}" onclick="setF('a',S.f.a==='${c[1]}'?'':'${c[1]}')">${c[0]} ${c[1]}</button>`).join('')}</div>
<div class="card"><div class="filters"><label>Buscar<input type="search" value="${f.q}" placeholder="Nome ou instituição" oninput="S.f.q=this.value;render(1)"></label>${sel('a','Área',CATS.map(c=>c[1]))}${sel('i','Instituição',[...new Set(C.map(c=>c.i))])}${sel('h','Carga horária',[['1','Até 20 h'],['2','21 a 30 h'],['3','Mais de 30 h']])}${sel('l','Nível',['Básico','Intermediário'])}${sel('m','Modalidade',['EaD','Autoinstrucional','Híbrido'])}<label class="ck"><input type="checkbox" ${f.free?'checked':''} onchange="setF('free',this.checked)"> Cursos gratuitos</label><label class="ck"><input type="checkbox" ${f.cert?'checked':''} onchange="setF('cert',this.checked)"> Com certificado</label><button class="btn o" onclick="clearF()">Limpar filtros</button></div></div>
<h2>${r.length} curso${r.length===1?'':'s'} encontrado${r.length===1?'':'s'}</h2>${r.length?`<div class="grid">${r.map(card).join('')}</div>`:`<div class="card">Nenhum curso demonstrativo com esses filtros. <button class="btn o" onclick="clearF()">Limpar filtros</button></div>`}`}
function vCursos(){const l=C.filter(isEn);return `<h1>Meus cursos</h1><div class="mu">Cursos em que você está inscrito.</div><h2></h2>${l.length?`<div class="grid">${l.map(card).join('')}</div>`:`<div class="card">Você ainda não se inscreveu. <button class="btn" onclick="go('explorar')">Explorar cursos</button></div>`}`}
function vCurso(){const c=byId(S.cid),ms=ML(c),n=S.en[c.id],en=isEn(c),dn=isDone(c);
return `<button class="btn o" onclick="go('explorar')">← Voltar</button><div class="row" style="margin-top:16px"><div><h1>${c.t}</h1><div class="mu">${c.i}</div></div><button class="fav sp" onclick="fav(${c.id})" style="font-size:26px">${S.fav.has(c.id)?'⭐':'☆'}</button></div><div class="tags" style="margin-top:10px"><span class="tag g">Gratuito</span><span class="tag p">Curso demonstrativo</span><span class="tag">${c.h} horas</span><span class="tag">${ms.length} módulos</span><span class="tag">${c.l}</span><span class="tag">${c.m}</span><span class="tag">Com certificado</span></div>
<div class="two"><div>${dn?`<div class="win"><h2 style="margin:0">Curso concluído!</h2><p>Certificado disponível.</p><button class="btn" onclick="showCert(${c.id})">Visualizar certificado</button></div>`:''}
<div class="card"><h3>Sobre o curso</h3><p class="mu">${c.d}</p><h3>Objetivos</h3><ul class="mu"><li>Compreender os conceitos centrais de ${c.a.toLowerCase()}.</li><li>Aplicar o conteúdo nas rotinas de trabalho.</li><li>Concluir todos os módulos para obter o certificado.</li></ul><h3>Requisitos</h3><p class="mu">Acesso à internet e interesse em serviço público. Nenhum conhecimento prévio.</p></div>
<h2>Conteúdo programático</h2>${ms.map((m,i)=>`<div class="mod ${en&&i<n?'done':''}"><span class="ck2">${en&&i<n?'✓':''}</span><div><b>Módulo ${i+1}: ${m}</b><div class="sm mu">${fmt(c.h/ms.length)} h</div></div>${en&&i===n?`<button class="btn sp" onclick="complete(${c.id})">Concluir módulo</button>`:''}</div>`).join('')}</div>
<div class="card" style="align-self:start"><h3>Seu progresso</h3><div class="bar"><i style="width:${pct(c)}%"></i></div><div class="sm mu">${pct(c)}% · ${n||0} de ${ms.length} módulos</div><br>${!en?`<button class="btn" onclick="enroll(${c.id})">Inscrever-se</button>`:dn?`<button class="btn" onclick="showCert(${c.id})">Ver certificado</button>`:`<button class="btn" onclick="complete(${c.id})">Continuar</button>`}<p class="sm mu">Este é um protótipo. Não há conteúdo real de curso.</p></div></div>`}
function vProg(){return `<h1>Meu progresso</h1><div class="mu">Acompanhe cada curso.</div><h2></h2>${C.filter(isEn).map(c=>`<div class="card" style="margin-bottom:12px"><div class="row"><b>${c.t}</b><span class="sp tag ${isDone(c)?'g':''}">${isDone(c)?'Concluído':'Em andamento'}</span></div><div class="bar"><i style="width:${pct(c)}%"></i></div><div class="row sm mu"><span>${pct(c)}% · ${S.en[c.id]}/${ML(c).length} módulos</span><button class="btn o sp" onclick="openC(${c.id})">Abrir</button></div></div>`).join('')||'<div class="card">Nenhum curso iniciado.</div>'}`}
function vCerts(){const l=C.filter(isDone);return `<h1>Certificados</h1><div class="mu">Certificados demonstrativos dos cursos concluídos.</div><h2></h2>${l.length?`<div class="grid">${l.map(c=>`<div class="card cc"><div style="font-size:30px">🏆</div><h3>${c.t}</h3><div class="mu sm">${c.i}</div><div class="tags"><span class="tag">${c.h} horas</span><span class="tag">Concluído em ${S.done[c.id]}</span></div><div class="sm">Código: <b>${code(c)}</b></div><button class="btn" onclick="showCert(${c.id})">Visualizar</button></div>`).join('')}</div>`:'<div class="card">Conclua um curso para receber seu certificado.</div>'}`}
function vFavs(){const l=C.filter(c=>S.fav.has(c.id));return `<h1>Favoritos</h1><h2></h2>${l.length?`<div class="grid">${l.map(card).join('')}</div>`:'<div class="card">Toque na estrela de um curso para guardá-lo aqui.</div>'}`}
function vInst(){return `<h1>Instituições</h1><div class="mu">Tipos de instituição usados no protótipo.</div><div class="note">Os nomes são genéricos e demonstrativos. Nenhuma instituição real está indicada como ofertante dos cursos.</div><div class="grid">${INST.map(x=>`<div class="card cc"><div style="font-size:28px">🏛️</div><h3>${x[0]}</h3><div class="mu sm">${x[1]}</div><span class="tag p" style="align-self:flex-start">Exemplo</span><button class="btn o" style="margin-top:auto" onclick="${x[2]?`clearF();S.f.i='${x[2]}';go('explorar')`:`toast('Sem cursos demonstrativos')`}">Ver cursos</button></div>`).join('')}</div>`}
function vDes(){const by={};C.forEach(c=>{if(isEn(c))by[c.a]=(by[c.a]||0)+S.en[c.id]*c.h/ML(c).length});const tot=hrs(),mx=Math.max(1,...Object.values(by));const mods=C.reduce((s,c)=>s+(isEn(c)?S.en[c.id]:0),0);
return `<h1>Meu desempenho</h1><div class="mu">Horas estudadas por área.</div><div class="stats" style="grid-template-columns:repeat(auto-fit,minmax(150px,1fr))"><div class="card stat"><b>${fmt(tot)} h</b><span class="sm mu">Total estudado</span></div><div class="card stat"><b>${mods}</b><span class="sm mu">Módulos concluídos</span></div><div class="card stat"><b>${C.filter(isDone).length}/${C.filter(isEn).length}</b><span class="sm mu">Cursos finalizados</span></div></div><h2>Por área</h2><div class="card">${Object.keys(by).map(k=>`<div class="dash"><span>${k}</span><div class="bar"><i style="width:${by[k]/mx*100}%"></i></div><b class="sm">${fmt(by[k])} h</b></div>`).join('')||'Sem dados ainda.'}</div>`}
function vPerfil(){return `<h1>Perfil</h1><div class="card" style="max-width:420px;margin-top:16px"><div class="row"><div class="av">${S.name[0]||'?'}</div><b>${S.name}</b></div><br><label class="sm mu">Seu nome<input type="text" value="${S.name}" onchange="S.name=this.value.trim()||'Marco';render()"></label><p class="sm mu">O nome aparece na saudação e nos certificados.</p><button class="btn p" onclick="if(confirm('Zerar todo o progresso?')){S.en={};S.done={};render();toast('Progresso zerado')}">Zerar progresso</button></div>`}
const V={home:vHome,cursos:vCursos,explorar:vExplorar,curso:vCurso,progresso:vProg,certs:vCerts,favs:vFavs,inst:vInst,desempenho:vDes,perfil:vPerfil};
const NK={curso:'explorar',progresso:'progresso'};
function render(keepFocus){
$('side').innerHTML=`<div class="logo">CAPACITA <b>GOV</b></div><div class="slog">Capacitação pública para transformar resultados.</div>${NAV.map(n=>`<button class="nav ${(S.v===n[0]||(S.v==='curso'&&n[0]==='explorar'))?'on':''}" onclick="go('${n[0]}')"><span>${n[1]}</span>${n[2]}</button>`).join('')}<div class="user"><div class="av">${S.name[0]||'?'}</div><div><b>${S.name}</b><div class="sm mu">${C.filter(isDone).length} certificado(s)</div></div></div>`;
const a=document.activeElement,pos=a&&a.type==='search'?a.selectionStart:0;
$('app').innerHTML=V[S.v]();
if(keepFocus){const s=$('app').querySelector('input[type=search]');if(s){s.focus();s.setSelectionRange(pos,pos)}}}
render();
</script>
</body>
</html>
'''

class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        b = HTML.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)
    def log_message(self, *a): pass

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", PORT), H) as srv:
    print(f"CAPACITA GOV rodando em http://localhost:{PORT}")
    threading.Timer(1, lambda: webbrowser.open(f"http://localhost:{PORT}")).start()
    srv.serve_forever()
