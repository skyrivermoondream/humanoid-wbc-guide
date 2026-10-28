#!/usr/bin/env python3
"""Builds the topic guide in two languages:
  index.html     English (default)
  zh/index.html  Chinese
Run from anywhere: python3 src/build.py
"""
import html
import json
from pathlib import Path

import content as C
import scene as S

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://skyrivermoondream.github.io/humanoid-wbc-guide/"
LANGS = {"en": ("index.html", "en", ""), "zh": ("zh/index.html", "zh-CN", "zh/")}
LANG = "en"
e = html.escape


def t(x):
    return x[LANG] if isinstance(x, dict) else x


def u(key, **kw):
    s = t(C.UI[key])
    return s.format(**kw) if kw else s


CSS = r"""
:root{
  --bg:#F7F9FC;--surface:#FFFFFF;--surface-2:#F0F4F9;
  --ink:#151B24;--ink-2:#354153;--muted:#5D6A7C;--line:#DFE5EC;--line-strong:#B6C1CF;
  --blue:#245BDF;--blue-ink:#23498C;--blue-pale:#EDF3FF;--blue-soft:#BCCFF3;--on-blue:#FFFFFF;
  --teal:#287F85;--teal-ink:#1D5E62;--teal-pale:#E4F2F2;--on-teal:#FFFFFF;
  --screen:#0E1726;
  --wall:#EEF2F7;--seam:#DDE4ED;--ceiling:#5A6677;--tray:#A3AFBD;--floor:#DCE3EB;--floor-edge:#3A4657;--lane:#C2CEDE;
  --steel:#98A4B3;--steel-dark:#69768A;--steel-light:#C7D0DB;--pipe:#8592A3;
  --cab:#C5CED9;--cab-door:#D8DFE8;--water:#CCDEF2;
  --robot:#25334A;--robot-far:#A1ADBD;--visor:#6FD0D3;--pack:#245BDF;--pack-led:#CFF3F3;
  --warn:#EFB13C;--needle:#E0533D;--led-g:#2FB27A;--led-r:#E0533D;
  --din:"DIN Alternate","Bahnschrift","Barlow Semi Condensed","Roboto Condensed","sans-serif-condensed","Arial Narrow",var(--font);
  color-scheme:light dark;
}
@media (prefers-color-scheme:dark){:root{
  --bg:#12151A;--surface:#191C22;--surface-2:#20252D;
  --ink:#E8EDF4;--ink-2:#C5CEDA;--muted:#A0ABBA;--line:#2E3642;--line-strong:#4B5667;
  --blue:#8AB2FF;--blue-ink:#D0DFFF;--blue-pale:#1E2A3E;--blue-soft:#435D88;--on-blue:#0B1426;
  --teal:#70C3C5;--teal-ink:#C3EBEC;--teal-pale:#17302F;--on-teal:#08201F;
  --screen:#0A0E14;
  --wall:#1A1F27;--seam:#252C36;--ceiling:#3B4553;--tray:#4C5767;--floor:#21272F;--floor-edge:#7B8799;--lane:#34404F;
  --steel:#5C6878;--steel-dark:#8692A3;--steel-light:#36404C;--pipe:#515D6C;
  --cab:#2A323D;--cab-door:#333C48;--water:#294462;
  --robot:#D2DAE5;--robot-far:#5A6677;--visor:#3AA7AC;--pack:#6E9BFF;--pack-led:#E8F7F7;
  --warn:#E3A537;--needle:#FF7A62;
}}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:68px}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/var(--lh) var(--font);-webkit-text-size-adjust:100%;overflow-x:clip}
a{color:var(--blue);text-underline-offset:3px;text-decoration-thickness:1px}
a:hover{text-decoration-thickness:2px}
:focus-visible{outline:2px solid var(--blue);outline-offset:2px;border-radius:4px}
h1,h2,h3,h4{line-height:1.25;margin:0;font-weight:750;letter-spacing:var(--hls)}
p{margin:0}
.wrap{max-width:1120px;margin:0 auto;padding:0 24px}
@media (max-width:600px){.wrap{padding:0 16px}}

/* top bar: a route line with one stop per section */
.bar{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.bar .wrap{display:flex;align-items:center;gap:16px;height:56px}
.brand{font-weight:700;font-size:15px;color:var(--ink);text-decoration:none;white-space:nowrap}
.brand span{font-family:var(--din);color:var(--muted);font-weight:600;margin-left:6px}
.nav{margin-left:auto;display:flex;align-self:stretch}
.nav a{position:relative;display:flex;align-items:center;padding:0 11px 2px;color:var(--muted);text-decoration:none;font-size:14px;white-space:nowrap}
.nav a::after{content:"";position:absolute;left:50%;bottom:-5px;width:9px;height:9px;margin-left:-4.5px;border-radius:50%;background:var(--surface);border:1.5px solid var(--line-strong)}
.nav a:hover{color:var(--ink)}
.nav a.on{color:var(--ink);font-weight:600}
.nav a.on::after{background:var(--blue);border-color:var(--blue)}
.lang{display:inline-flex;flex:none;border:1px solid var(--blue-soft);border-radius:7px;overflow:hidden;background:var(--blue-pale);font-size:13px;line-height:1}
.lang a,.lang span{display:block;padding:6px 9px;text-decoration:none;color:var(--blue-ink)}
.lang span{background:var(--blue);color:var(--on-blue);font-weight:600}
.lang a:hover{background:var(--surface)}
@media (max-width:720px){.brand span{display:none}.bar .wrap{gap:10px}.nav a{padding:0 8px 2px}}
@media (max-width:600px){.brand{display:none}.nav{margin-left:0;flex:1;justify-content:space-between}.nav a{padding:0 4px 2px;font-size:13.5px}.lang a,.lang span{padding:6px 8px}}
@media (max-width:380px){.nav a{padding:0 2px 2px;font-size:13px}.lang a,.lang span{padding:6px 7px}}

/* hero */
.hero{padding-top:48px;padding-bottom:8px}
.hero-top{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:40px;align-items:end}
.hero h1{font-size:clamp(32px,5vw,52px);line-height:1.12}
.nw{white-space:nowrap}
.hero h1 small{display:block;font-size:.5em;font-weight:600;color:var(--ink-2);margin-top:10px;letter-spacing:0}
.lede{margin-top:18px;font-size:17px;color:var(--ink-2);max-width:34em}
.spec{background:var(--blue-pale);padding:18px 22px;border-radius:12px}
.spec p{font-size:17px;line-height:1.65}
.spec b{color:var(--blue-ink)}
.spec .meta{margin-top:10px;font-size:13px;color:var(--muted)}
@media (max-width:860px){.hero-top{grid-template-columns:1fr;gap:20px}}
.scene-box{margin-top:28px;border:1px solid var(--line);border-radius:14px;background:var(--wall);overflow-x:auto;overflow-y:hidden;-webkit-overflow-scrolling:touch}
.scene{display:block;width:100%;min-width:760px;height:auto}
.swipe{display:none;font-size:13px;color:var(--muted);margin-top:6px}
@media (max-width:760px){.swipe{display:block}}
.legend{list-style:none;padding:0;margin:16px 0 0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px 20px}
.legend a{display:flex;gap:10px;align-items:center;color:var(--ink);text-decoration:none;padding:4px 0;font-size:15px;line-height:1.35}
.legend a:hover span:last-child{text-decoration:underline}
@media (max-width:760px){.legend{grid-template-columns:1fr 1fr}}
@media (max-width:440px){.legend{grid-template-columns:1fr}}
.pin{flex:none;display:inline-grid;place-items:center;width:26px;height:26px;border-radius:50%;background:var(--teal);color:var(--on-teal);font:700 14px/1 var(--din)}

/* scene artwork */
.sc-wall{fill:var(--wall)}.sc-seam{stroke:var(--seam);stroke-width:1.5}
.sc-ceiling{fill:var(--ceiling)}.sc-tray{fill:none;stroke:var(--tray);stroke-width:2.5}.sc-tray-rib{stroke:var(--tray);stroke-width:2}
.sc-floor{fill:var(--floor)}.sc-floor-edge{stroke:var(--floor-edge);stroke-width:2}.sc-lane{stroke:var(--lane);stroke-width:3;stroke-dasharray:22 14}
.sc-water{fill:var(--water)}.sc-water-glint{stroke:#fff;stroke-width:2.5;stroke-linecap:round;opacity:.85}
.sc-step{fill:var(--steel-light);stroke:var(--steel-dark);stroke-width:1.5}.sc-grate{stroke:var(--steel-dark);stroke-width:2}.sc-step-edge{stroke:var(--warn);stroke-width:3}
.sc-hanger{stroke:var(--steel-dark);stroke-width:4}.sc-pipe{fill:var(--pipe)}.sc-pipe-0{fill:var(--steel)}.sc-pipe-2{fill:var(--steel-dark)}.sc-clamp{fill:var(--steel-dark)}
.sc-hazard rect{fill:var(--warn)}.sc-hazard-stripe{stroke:#1B2230;stroke-width:3}
.sc-gauge-ring{fill:var(--steel-dark)}.sc-gauge-face{fill:#F7F9FB}.sc-needle{stroke:var(--needle);stroke-width:3;stroke-linecap:round}.sc-gauge-arc{fill:none;stroke:#287F85;stroke-width:3}
.sc-cabinet{fill:var(--cab);stroke:var(--floor-edge);stroke-width:1.5}.sc-door{fill:var(--cab-door);stroke:var(--steel-dark);stroke-width:1.5}.sc-handle{fill:var(--robot)}
.sc-led-g{fill:var(--led-g)}.sc-led-y{fill:var(--warn)}.sc-led-o{fill:var(--led-r)}
.sc-warn{fill:var(--warn);stroke:#1B2230;stroke-width:2;stroke-linejoin:round}.sc-warn-bolt{fill:none;stroke:#1B2230;stroke-width:2;stroke-linejoin:round}
.sc-vent{stroke:var(--steel-dark);stroke-width:2;opacity:.5}
.sc-booth-box{fill:var(--surface);stroke:var(--line-strong);stroke-width:1.5}.sc-screen{fill:var(--screen)}.sc-screen-line{fill:none;stroke:#70C3C5;stroke-width:2.5;stroke-linejoin:round}
.sc-op{fill:none;stroke:var(--ink-2);stroke-width:2.5}.sc-vr{fill:var(--teal)}.sc-signal{fill:none;stroke:var(--blue);stroke-width:2.5;stroke-linecap:round}
.sc-link{fill:none;stroke:var(--blue);stroke-width:2;stroke-dasharray:6 7;stroke-linecap:round;opacity:.8}
.sc-sight{stroke:var(--teal);stroke-width:2;stroke-dasharray:4 6}
.sc-leader{stroke:var(--ink-2);stroke-width:1.4}
.rb-near{stroke:var(--robot)}.rb-near-fill{fill:var(--robot)}.rb-far{stroke:var(--robot-far)}.rb-far-fill{fill:var(--robot-far)}
.rb-body{fill:var(--robot)}.rb-trim{stroke:var(--visor)}.rb-visor{fill:var(--visor)}.rb-pack{fill:var(--pack)}
.rb-pack-line{fill:#fff;opacity:.35}.rb-led{fill:var(--pack-led)}.rb-ant{stroke:var(--pack)}
@media (prefers-color-scheme:dark){.sc-water-glint{opacity:.3}}
.hero-route{fill:none;stroke:var(--teal);stroke-width:6;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:0}
.sc-mark{cursor:pointer}
.sc-mark circle{fill:var(--teal);stroke:var(--wall);stroke-width:4;transition:transform .15s}
.sc-mark text{font:700 18px var(--din);fill:var(--on-teal);text-anchor:middle;pointer-events:none}
.sc-mark circle,.sc-mark{transform-box:fill-box;transform-origin:center}
.sc-mark:hover circle,.sc-mark:focus-visible circle{transform:scale(1.15)}
@media (prefers-reduced-motion:no-preference){
  .hero-route{stroke-dashoffset:1;animation:walk 1.9s .25s cubic-bezier(.55,0,.25,1) forwards}
  .hero .sc-mark{animation:pop .5s calc(.55s + var(--i) * .2s) both}
}
@keyframes walk{to{stroke-dashoffset:0}}
@keyframes pop{from{opacity:0;transform:translateY(6px) scale(.5)}to{opacity:1;transform:none}}

/* sections */
.station{padding-top:76px;padding-bottom:8px}
.st-head{display:grid;grid-template-columns:auto 1fr;gap:6px 18px;align-items:center;margin-bottom:28px}
.st-no{position:relative;display:grid;place-items:center;width:46px;height:46px;border-radius:50%;background:var(--blue);color:var(--on-blue);font:700 22px/1 var(--din)}
.st-no::before{content:"";position:absolute;right:100%;top:50%;margin-top:-1px;width:100vw;height:2px;background:var(--blue-soft);z-index:-1}
.st-head h2{font-size:clamp(25px,3.3vw,33px)}
.st-head p{grid-column:2;color:var(--muted);font-size:16px;max-width:44em}
@media (max-width:600px){.st-no{width:40px;height:40px;font-size:19px}.st-head p{grid-column:1 / -1}}
.sub-h{font-size:21px;margin:52px 0 6px}
.sub-p{color:var(--muted);max-width:46em;margin-bottom:22px}

/* pipeline */
.pipe{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:18px;position:relative}
.pipe::before{content:"";position:absolute;left:32px;right:32px;top:32px;height:2px;background:var(--line-strong)}
.stage{position:relative;display:flex;flex-direction:column;align-items:flex-start}
.stage .ic{position:relative;display:grid;place-items:center;width:64px;height:64px;border-radius:50%;background:var(--surface);border:1.5px solid var(--blue-soft)}
.stage .ic .n{position:absolute;top:-5px;left:-5px;width:22px;height:22px;border-radius:50%;display:grid;place-items:center;background:var(--blue);color:var(--on-blue);font:700 12px/1 var(--din)}
.ico{width:36px;height:36px;stroke:var(--ink-2);stroke-width:2.3}
.ico .i-dot{fill:var(--blue);stroke:none}.ico .i-thin{stroke-width:1.5;opacity:.6}.ico .i-dash{stroke-dasharray:3 3}
.stage h3{font-size:17px;margin-top:14px}
.stage .alias{font-size:13px;color:var(--blue-ink);background:var(--blue-pale);padding:1px 8px;border-radius:4px;margin-top:5px;line-height:1.6}
.stage p{font-size:14.5px;color:var(--ink-2);margin-top:8px}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
.wk{display:inline-flex;align-items:center;gap:6px;font:600 13px/1 var(--din);padding:6px 10px;border:1px solid var(--line);border-radius:999px;color:var(--ink);text-decoration:none;background:var(--surface)}
.wk::before{content:"";width:7px;height:7px;border-radius:50%;background:var(--line-strong)}
.wk[data-g=onegs]::before{background:var(--blue)}
.wk:hover{border-color:var(--blue-soft);color:var(--blue-ink)}
@media (max-width:1000px){.pipe{grid-template-columns:repeat(3,minmax(0,1fr));row-gap:36px}.pipe::before{display:none}}
@media (max-width:620px){.pipe{grid-template-columns:1fr;row-gap:24px}
  .pipe::before{display:block;left:31px;right:auto;top:32px;bottom:32px;width:2px;height:auto}
  .stage{display:grid;grid-template-columns:64px 1fr;gap:0 16px;align-items:start}.stage .ic{grid-row:span 4}.stage h3{margin-top:2px}.stage .alias{justify-self:start}}

/* the three lines ONE-G builds on */
.trio{display:grid;grid-template-columns:1fr 36px 1.15fr 36px 1fr;align-items:stretch}
.leg{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:18px 20px 20px;display:flex;flex-direction:column}
.leg.core{border:1.5px solid var(--blue)}
.leg .role{font-size:13px;color:var(--muted)}
.leg h3{font:700 24px/1.2 var(--din);margin:2px 0 4px}
.leg p{font-size:14.5px;color:var(--ink-2);margin-top:8px}
.leg .chips{margin-top:auto;padding-top:12px}
.leg svg{display:block;width:100%;height:auto;margin:12px 0 4px}
.arrow{display:grid;place-items:center;color:var(--line-strong)}
.arrow svg{width:28px;height:28px}
.gpu-cell{fill:var(--line-strong)}.gpu-one{fill:var(--blue)}
.dia-t{font:600 13px var(--din);fill:var(--muted)}.dia-t.ink{fill:var(--ink)}
.lora{fill:var(--blue-pale);stroke:var(--blue-soft);stroke-width:1.5}.lora-t{font:700 12.5px var(--din);fill:var(--blue-ink)}
.dia-arrow{fill:none;stroke:var(--ink-2);stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.in-chip{fill:var(--surface-2);stroke:var(--line)}
.trio-note{margin-top:18px;padding:14px 18px;background:var(--blue-pale);border-radius:10px;color:var(--ink);max-width:58em}
@media (max-width:900px){.trio{grid-template-columns:1fr}.arrow{height:36px}.arrow svg{transform:rotate(90deg)}}

/* works */
.filters{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:22px}
.filter{font:inherit;font-size:14px;line-height:1.3;cursor:pointer;display:inline-flex;align-items:center;gap:8px;padding:7px 14px;border-radius:999px;border:1px solid var(--line-strong);background:var(--surface);color:var(--ink)}
.filter .c{font-family:var(--din);color:var(--muted)}
.filter:hover{border-color:var(--blue-soft)}
.filter[aria-pressed=true]{background:var(--blue);color:var(--on-blue);border-color:var(--blue)}
.filter[aria-pressed=true] .c{color:inherit;opacity:.75}
.works{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;align-items:start}
@media (max-width:900px){.works{grid-template-columns:1fr}}
.work{background:var(--surface);border:1px solid var(--line);border-radius:14px;overflow:hidden;scroll-margin-top:76px}
.work[hidden]{display:none}
.work[data-g=onegs]{border-color:var(--blue-soft)}
.plate{display:flex;flex-wrap:wrap;align-items:center;gap:6px 12px;padding:14px 16px 4px}
.work[data-g=onegs] .plate{background:var(--blue-pale);padding-bottom:12px}
.plate h3{font:700 25px/1.15 var(--din)}
.plate h3 small{font-size:14px;font-weight:600;color:var(--muted);margin-left:8px}
.plate .venue{margin-left:auto;font-size:12.5px;font-weight:600;padding:3px 10px;border-radius:999px;border:1px solid var(--line);color:var(--ink-2);background:var(--surface);white-space:nowrap}
.org{padding:8px 16px 0;font-size:13.5px;color:var(--muted);display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.follow{font-size:12px;font-weight:600;color:var(--on-blue);background:var(--blue);padding:2px 9px;border-radius:999px}
.media{margin:12px 16px 0}
.screen{position:relative;aspect-ratio:16/9;background:var(--screen);border-radius:10px;overflow:hidden}
.screen video{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;background:var(--screen)}
.play{position:absolute;inset:0;margin:auto;width:max-content;height:max-content;display:flex;align-items:center;gap:9px;padding:9px 17px 9px 10px;border-radius:999px;border:0;background:var(--blue);color:var(--on-blue);font:inherit;font-size:15px;font-weight:600;cursor:pointer;box-shadow:0 6px 18px rgb(0 0 0 / .28)}
.play svg{width:24px;height:24px}
.play .pc{fill:var(--on-blue)}.play .pt{fill:var(--blue)}
.play:hover{transform:scale(1.04)}
.media.is-playing .play{display:none}
.fail{position:absolute;inset:0;display:none;place-content:center;text-align:center;padding:16px;color:#E8EDF4;font-size:14px;gap:8px}
.fail a{color:#8AB2FF}
.media.is-error .fail{display:grid}.media.is-error .play,.media.is-error video{display:none}
.clips{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.clip{font:inherit;font-size:13px;line-height:1.4;white-space:nowrap;cursor:pointer;padding:4px 10px;border-radius:6px;border:1px solid var(--line);background:var(--surface);color:var(--ink-2)}
.clip:hover{border-color:var(--blue-soft)}
.clip[aria-selected=true]{background:var(--blue);border-color:var(--blue);color:var(--on-blue)}
.media figcaption{font-size:12px;color:var(--muted);margin-top:6px;line-height:1.5}
.media figcaption a{color:inherit}
.body{padding:14px 16px 18px}
.body .one{font-size:15.5px}
.explain{margin:12px 0 0;display:grid;grid-template-columns:max-content minmax(0,1fr);gap:8px 14px;font-size:14.5px}
.explain dt{font-weight:700;color:var(--muted)}
.explain dd{margin:0;color:var(--ink-2)}
.explain dt.ins{color:var(--teal)}
@media (max-width:440px){.explain{grid-template-columns:1fr;gap:0}.explain dd{margin-bottom:8px}}
.nums{list-style:none;padding:0;margin:14px 0 0;display:flex;flex-wrap:wrap;gap:6px}
.nums li{font:600 13px/1.2 var(--din);padding:5px 9px;background:var(--surface-2);color:var(--ink-2);border-radius:6px}
.links{margin-top:14px;display:flex;flex-wrap:wrap;gap:4px 16px;font-size:14px}
.work.flash{animation:flash 1.4s ease-out}
@keyframes flash{0%,30%{box-shadow:0 0 0 4px var(--blue-soft)}100%{box-shadow:0 0 0 0 transparent}}
.stack{position:absolute;inset:0;display:grid;align-content:center;gap:8px;padding:18px 22px}
.stack div{border:1px solid #4B5667;color:#E8EDF4;border-radius:8px;padding:8px 12px;font-size:14px;display:flex;justify-content:space-between;gap:10px}
.stack div b{font-family:var(--din)}
.stack div:nth-child(2){border-color:#8AB2FF}
.stack .cmd{border-style:dashed;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12.5px;color:#9FE0E2}

/* needs */
.needs{border-top:1px solid var(--line)}
.need{display:grid;grid-template-columns:200px minmax(0,1fr) minmax(0,.95fr);gap:22px;padding:22px 0;border-bottom:1px solid var(--line);scroll-margin-top:76px}
.need .thumb{position:relative;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:var(--wall);aspect-ratio:4/3}
.need .thumb svg{display:block;width:100%;height:100%}
.need .thumb .pin{position:absolute;left:8px;top:8px}
.need h3{font-size:19px}
.need .desc{color:var(--ink-2);margin-top:6px;font-size:15px}
.need dl{margin:0;display:grid;gap:10px;font-size:14.5px}
.need dt{font-size:13px;color:var(--muted);font-weight:700}
.need dd{margin:2px 0 0}
.tp{display:inline-flex;align-items:center;gap:7px;font-size:13.5px;font-weight:600;color:var(--teal-ink);text-decoration:none;padding:4px 10px 4px 4px;border-radius:6px;background:var(--teal-pale);line-height:1.35}
.tp b{flex:none;display:inline-grid;place-items:center;width:20px;height:20px;border-radius:4px;background:var(--teal);color:var(--on-teal);font:700 12px/1 var(--din)}
.tp:hover{text-decoration:underline}
.need-split{margin:34px 0 0;padding-bottom:4px;font-size:15px;font-weight:700;color:var(--muted)}
@media (max-width:900px){.need{grid-template-columns:150px minmax(0,1fr)}.need dl{grid-column:1 / -1}}
@media (max-width:520px){.need{grid-template-columns:1fr}.need .thumb{max-width:260px}}

/* topics */
.chooser{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin-bottom:22px}
.chooser p{font-weight:600}
.choices{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.choice{font:inherit;font-size:14.5px;line-height:1.3;cursor:pointer;padding:8px 15px;border-radius:999px;border:1px solid var(--line-strong);background:var(--surface);color:var(--ink)}
.choice:hover{border-color:var(--teal)}
.choice[aria-pressed=true]{background:var(--teal);color:var(--on-teal);border-color:var(--teal);font-weight:600}
#choice-out{margin-top:10px;font-size:14.5px;color:var(--ink-2);min-height:1.5em;font-weight:400}
.topics{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}
@media (max-width:900px){.topics{grid-template-columns:1fr}}
.topic{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:0 0 18px;transition:opacity .2s;scroll-margin-top:76px}
.topic.dim{opacity:.35}
.t-head{display:grid;grid-template-columns:auto 1fr auto;gap:2px 14px;align-items:center;padding:16px 18px 14px;border-bottom:1px solid var(--line)}
.t-letter{grid-row:span 2;display:grid;place-items:center;width:44px;height:44px;border-radius:10px;background:var(--teal);color:var(--on-teal);font:700 22px/1 var(--din)}
.t-head h3{font-size:18.5px}
.t-head .sub{font-size:13.5px;color:var(--muted);grid-column:2;line-height:1.45}
.lvl{grid-row:span 2;text-align:right;font-size:12.5px;color:var(--muted);font-weight:600;white-space:nowrap}
.lvl i{display:flex;gap:3px;justify-content:flex-end;margin-bottom:4px}
.lvl i span{width:14px;height:6px;border-radius:3px;background:var(--line)}
.lvl i span.on{background:var(--teal)}
.t-body{padding:14px 18px 0}
.t-body .one{font-size:15.5px}
.t-body dl{margin:12px 0 0;display:grid;gap:12px;font-size:14.5px}
.t-body dt{font-size:13px;color:var(--muted);font-weight:700}
.t-body dd{margin:3px 0 0;color:var(--ink-2)}
.t-body ol{margin:4px 0 0;padding-left:1.4em}
.t-body li{margin:2px 0}
.fit{font-size:13px;color:var(--muted);margin-top:6px}
.onegs-note{margin-top:20px;font-size:14.5px;color:var(--muted)}
@media (max-width:440px){.t-head{grid-template-columns:auto 1fr}.lvl{grid-row:auto;grid-column:1 / -1;text-align:left;margin-top:8px}.lvl i{justify-content:flex-start}}

/* first month */
.weeks{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:22px;position:relative}
.weeks::before{content:"";position:absolute;left:21px;right:21px;top:20px;height:2px;background:var(--blue-soft)}
.week .w{position:relative;display:grid;place-items:center;width:42px;height:42px;border-radius:50%;background:var(--surface);border:2px solid var(--blue);font:700 15px/1 var(--din);color:var(--blue)}
.week h3{font-size:17px;margin-top:12px}
.week p{font-size:14.5px;color:var(--ink-2);margin-top:6px}
@media (max-width:860px){.weeks{grid-template-columns:1fr 1fr;row-gap:28px}.weeks::before{display:none}}
@media (max-width:520px){.weeks{grid-template-columns:1fr}}
.res{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;margin-top:8px}
.res h4{margin:0 0 6px;font-size:15px}
.res ul{margin:0;padding-left:1.1em;font-size:14.5px}
.res .tip{font-size:13px;color:var(--muted);margin-top:8px}
code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12.5px;background:var(--surface-2);padding:1px 5px;border-radius:4px}
@media (max-width:760px){.res{grid-template-columns:1fr}}
.gloss-sub{color:var(--muted);font-size:14.5px;margin-bottom:8px}
.gloss{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 28px;margin:0}
.gloss div{padding:10px 0;border-bottom:1px solid var(--line)}
.gloss dt{font-weight:700;font-size:15px}
.gloss dt span{font-weight:400;color:var(--muted);margin-left:8px;font-size:14px}
.gloss dd{margin:2px 0 0;font-size:14.5px;color:var(--ink-2)}
@media (max-width:700px){.gloss{grid-template-columns:1fr}}

footer{margin-top:84px;border-top:1px solid var(--line);background:var(--surface);padding:28px 0 40px;font-size:13.5px;color:var(--muted)}
footer h2{font-size:15px;color:var(--ink);margin-bottom:8px;letter-spacing:0}
.src{columns:2;column-gap:28px;padding-left:1.2em;margin:0 0 18px}
.src li{break-inside:avoid;margin:2px 0}
@media (max-width:700px){.src{columns:1}}
"""

FONTS = {
    "en": dict(font='-apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI Variable Text","Segoe UI",system-ui,Roboto,'
                    '"Helvetica Neue",Arial,"PingFang SC","Microsoft YaHei","Noto Sans SC",sans-serif',
               lh="1.6", hls="-0.015em"),
    "zh": dict(font='"PingFang SC","HarmonyOS Sans SC","MiSans","Microsoft YaHei UI","Microsoft YaHei","Noto Sans SC",'
                    '"Noto Sans CJK SC","Source Han Sans SC",-apple-system,system-ui,sans-serif',
               lh="1.75", hls="0.01em"),
}

JS = r"""
(() => {
  const L = __I18N__;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // language switch keeps the section you are reading
  $$('.lang a').forEach(a => a.addEventListener('click', () => { a.href = a.getAttribute('href').split('#')[0] + location.hash; }));

  // videos: show a first frame when near the viewport, play only on request
  function prime(fig) {
    const v = $('video', fig);
    if (!v || v.dataset.primed) return;
    v.dataset.primed = '1';
    load(v, $('.clip[aria-selected="true"]', fig) || $('.clip', fig), false);
  }
  function load(v, tab, play) {
    const fig = v.closest('.media');
    fig.classList.remove('is-error');
    v.poster = tab.dataset.poster || '';
    v.preload = play ? 'auto' : 'metadata';
    v.src = tab.dataset.src + (play ? '' : '#t=0.1');
    $('.fail a', fig).href = tab.dataset.page;
    if (play) start(v);
  }
  function start(v) {
    v.closest('.media').classList.add('is-playing');
    v.controls = true;
    const p = v.play();
    if (p && p.catch) p.catch(() => {});
  }
  const io = 'IntersectionObserver' in window
    ? new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) { prime(en.target); io.unobserve(en.target); } }), { rootMargin: '300px 0px' })
    : null;
  $$('.media').forEach(fig => {
    const v = $('video', fig);
    if (!v) return;
    io ? io.observe(fig) : prime(fig);
    $('.play', fig).addEventListener('click', () => { prime(fig); start(v); });
    $$('.clip', fig).forEach(b => b.addEventListener('click', () => {
      $$('.clip', fig).forEach(x => x.setAttribute('aria-selected', String(x === b)));
      v.dataset.primed = '1';
      load(v, b, true);
    }));
    v.addEventListener('error', () => { fig.classList.add('is-error'); fig.classList.remove('is-playing'); });
  });

  // work filters
  const filters = $$('.filter');
  function setFilter(g) {
    filters.forEach(x => x.setAttribute('aria-pressed', String(x.dataset.g === g)));
    $$('.work').forEach(c => { c.hidden = !(g === 'all' || c.dataset.g === g); });
  }
  filters.forEach(b => b.addEventListener('click', () => setFilter(b.dataset.g)));

  // any link to a work card: reveal it, scroll to it, flash once
  document.addEventListener('click', ev => {
    const a = ev.target.closest('a[href^="#w-"]');
    if (!a) return;
    const card = document.getElementById(a.getAttribute('href').slice(1));
    if (!card) return;
    ev.preventDefault();
    if (card.hidden) setFilter('all');
    card.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    card.classList.remove('flash'); void card.offsetWidth; card.classList.add('flash');
    history.replaceState(null, '', '#' + card.id);
  });

  // topic chooser
  const out = $('#choice-out');
  $$('.choice').forEach(b => b.addEventListener('click', () => {
    const on = b.getAttribute('aria-pressed') !== 'true';
    $$('.choice').forEach(x => x.setAttribute('aria-pressed', 'false'));
    b.setAttribute('aria-pressed', String(on));
    const tag = on ? b.dataset.tag : null;
    const hits = [];
    $$('.topic').forEach(tp => {
      const hit = !tag || tp.dataset.tags.split(' ').includes(tag);
      tp.classList.toggle('dim', !hit);
      if (tag && hit) hits.push(tp.dataset.letter);
    });
    out.textContent = tag ? L.out.replace('{list}', hits.join(L.sep)) : '';
  }));

  // highlight the current stop in the top bar
  const links = $$('.nav a');
  if ('IntersectionObserver' in window) {
    const spy = new IntersectionObserver(es => es.forEach(en => {
      if (en.isIntersecting) links.forEach(a => a.classList.toggle('on', a.hash === '#' + en.target.id));
    }), { rootMargin: '-40% 0px -55% 0px' });
    links.forEach(a => { const s = document.querySelector(a.hash); if (s) spy.observe(s); });
    const hero = document.getElementById('top');
    if (hero) new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) links.forEach(a => a.classList.remove('on')); }), { rootMargin: '-40% 0px -55% 0px' }).observe(hero);
  }
})();
"""

PLAY_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><circle class="pc" cx="12" cy="12" r="11"/>'
            '<path class="pt" d="M10 8 L16 12 L10 16 Z"/></svg>')
ARROW_SVG = ('<svg viewBox="0 0 32 32" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" '
             'stroke-linecap="round" stroke-linejoin="round"><path d="M5 16 H26 M19 9 L26 16 L19 23"/></svg>')
STAND = dict(lean=0, near_leg=(8, 4), far_leg=(-8, -5), near_arm=(-8, 6), far_arm=(10, 20))


def stand(x, ground, scale, pose=None):
    """A standing robot whose feet touch `ground` after scaling about the pelvis."""
    pose = pose or STAND
    near, far = S.ankle_offsets(pose)
    return S.robot((x, ground - max(near[1], far[1]) * scale), pose, scale=scale)


def wk(wid):
    w = C.WORK[wid]
    return f'<a class="wk" data-g="{w["group"]}" href="#w-{wid}">{e(w["name"])}</a>'


def tp(tid):
    tpc = C.TOPIC[tid]
    return f'<a class="tp" href="#t-{tid}"><b>{tid.upper()}</b>{e(t(tpc["title"]))}</a>'


def hero():
    labels = {n["n"]: e(t(n["title"])) for n in C.NEEDS}
    legend = "".join(
        f'<li><a href="#need-{n}"><span class="pin">{n}</span><span>{labels[n]}</span></a></li>' for n in range(1, 7))
    return f'''
<header class="hero wrap" id="top">
  <div class="hero-top">
    <div>
      <h1>{e(u("h1")).replace("Whole-Body", '<span class="nw">Whole-Body</span>')}<small>{e(u("h1_sub"))}</small></h1>
      <p class="lede">{e(u("lede"))}</p>
    </div>
    <div class="spec">
      <p><b>{e(u("spec_k"))}</b>{"" if LANG == "zh" else " "}{e(u("spec_v"))}</p>
      <p class="meta">{e(u("spec_meta"))}</p>
    </div>
  </div>
  <div class="scene-box">
    <svg class="scene" viewBox="0 0 1200 560" role="img" aria-labelledby="scene-title">
      <title id="scene-title">{e(u("scene_title"))}</title>
      <use href="#scene" width="1200" height="560"/>
      {S.hero_overlay(labels)}
    </svg>
  </div>
  <p class="swipe">{e(u("swipe"))}</p>
  <ol class="legend" aria-label="{e(u("legend_label"))}">{legend}</ol>
</header>'''


def section_head(no, sid, title, sub):
    return (f'<div class="st-head"><span class="st-no" aria-hidden="true">{no}</span>'
            f'<h2 id="{sid}-h">{e(title)}</h2><p>{e(sub)}</p></div>')


def primer():
    stages = []
    for i, (ic, name, alias, desc, works) in enumerate(C.STAGES, 1):
        stages.append(
            f'<li class="stage"><div class="ic"><span class="n">{i}</span>{S.icon(ic)}</div>'
            f'<h3>{e(t(name))}</h3><span class="alias">{e(u("alias_prefix"))}{e(t(alias))}</span><p>{e(t(desc))}</p>'
            f'<div class="chips">{"".join(wk(w) for w in works)}</div></li>')

    cells = "".join(f'<rect x="{c * 15}" y="{r * 11}" width="12" height="8" rx="1.5" class="gpu-cell"/>'
                    for r in range(8) for c in range(16))
    gpu = (f'<svg viewBox="0 0 300 110" aria-hidden="true"><g transform="translate(0 4)">{cells}</g>'
           f'<text x="0" y="106" class="dia-t">{e(u("dia_sonic_gpus"))}</text>'
           f'<rect x="264" y="36" width="24" height="16" rx="2" class="gpu-one"/>'
           f'<text x="298" y="106" class="dia-t ink" text-anchor="end">{e(u("dia_one_gpu"))}</text></svg>')
    sonic_robot = stand(166, 160, 0.55, dict(lean=2, near_arm=(-20, 10), far_arm=(18, 30), near_leg=(10, 4), far_leg=(-8, -6)))
    ins = ""
    for i, lab in enumerate(t(x) for x in C.UI["dia_inputs"]):
        y = 18 + i * 34
        ins += (f'<rect x="0" y="{y}" width="104" height="24" rx="12" class="in-chip"/>'
                f'<text x="52" y="{y + 16.5}" class="dia-t ink" text-anchor="middle">{e(lab)}</text>'
                f'<path d="M108 {y + 12} C 124 {y + 12}, 122 80, 134 80" class="dia-arrow" stroke-width="1.5" opacity=".5"/>')
    pol = [t(x) for x in C.UI["dia_policy"]]
    sonic = (f'<svg viewBox="0 0 300 168" aria-hidden="true">{ins}'
             f'<path d="M136 80 h4" class="dia-arrow"/>{sonic_robot}'
             f'<text x="204" y="72" class="dia-t">{e(pol[0])}</text><text x="204" y="90" class="dia-t ink">{e(pol[1])}</text></svg>')
    a2a = (f'<svg viewBox="0 0 300 168" aria-hidden="true">{stand(62, 146, 0.42)}{stand(232, 146, 0.55)}'
           f'<path d="M104 92 H172 M164 84 L173 92 L164 100" class="dia-arrow"/>'
           f'<rect x="118" y="104" width="42" height="20" rx="4" class="lora"/>'
           f'<text x="139" y="118.5" class="lora-t" text-anchor="middle">LoRA</text>'
           f'<text x="62" y="164" class="dia-t" text-anchor="middle">G1</text>'
           f'<text x="232" y="164" class="dia-t ink" text-anchor="middle">{e(u("dia_new"))}</text></svg>')
    return f'''
<section class="station wrap" id="s1" aria-labelledby="s1-h">
  {section_head(1, "s1", u("s1"), u("s1_sub"))}
  <ol class="pipe">{"".join(stages)}</ol>
  <h3 class="sub-h">{e(u("trio_h"))}</h3>
  <p class="sub-p">{e(u("trio_p"))}</p>
  <div class="trio">
    <div class="leg"><span class="role">{e(u("trio_sm_role"))}</span><h3>SuperMimic</h3>{gpu}
      <p>{e(u("trio_sm"))}</p><div class="chips">{wk("supermimic")}</div></div>
    <div class="arrow" aria-hidden="true">{ARROW_SVG}</div>
    <div class="leg core"><span class="role">{e(u("trio_sonic_role"))}</span><h3>SONIC</h3>{sonic}
      <p>{e(u("trio_sonic"))}</p><div class="chips">{wk("sonic")}</div></div>
    <div class="arrow" aria-hidden="true">{ARROW_SVG}</div>
    <div class="leg"><span class="role">{e(u("trio_a2a_role"))}</span><h3>Any2Any</h3>{a2a}
      <p>{e(u("trio_a2a"))}</p><div class="chips">{wk("any2any")}</div></div>
  </div>
  <p class="trio-note">{e(u("trio_note"))}</p>
</section>'''


def media(w):
    if not w["clips"]:
        rows = "".join(f'<div><span>{e(t(a))}</span><b>{e(t(b))}</b></div>' for a, b in C.UI["mj_rows"])
        return (f'<div class="media"><div class="screen"><div class="stack">{rows}'
                f'<div class="cmd">uvx --from mjlab --refresh demo</div></div></div>'
                f'<figcaption>{e(u("mj_caption"))}</figcaption></div>')
    tabs = []
    for i, (label, src, poster) in enumerate(w["clips"]):
        tabs.append(f'<button type="button" class="clip" role="tab" aria-selected="{"true" if i == 0 else "false"}" '
                    f'data-src="{e(src)}" data-poster="{e(poster or "")}" data-page="{e(w["page"])}">{e(t(label))}</button>')
    first = w["clips"][0]
    note = t(w["clip_note"]) if w.get("clip_note") else u("clip_note", name=w["name"])
    if len(tabs) > 1:
        clips_row = f'<div class="clips" role="tablist" aria-label="{e(u("clips_label", name=w["name"]))}">{"".join(tabs)}</div>'
    else:
        clips_row = tabs[0].replace('class="clip"', 'class="clip" hidden')
    poster = f' poster="{e(first[2])}"' if first[2] else ""
    return (f'<figure class="media"><div class="screen">'
            f'<video muted playsinline preload="none"{poster}></video>'
            f'<button type="button" class="play" aria-label="{e(u("play_aria", name=w["name"]))}">{PLAY_SVG}<span>{e(u("play"))}</span></button>'
            f'<div class="fail"><span>{e(u("fail"))}</span><a href="{e(w["page"])}" target="_blank" rel="noopener">{e(u("fail_link"))}</a></div>'
            f'</div>{clips_row}'
            f'<figcaption>{e(note)}{e(u("caption_tail"))} <a href="{e(w["page"])}" target="_blank" rel="noopener">{e(u("open_page"))}</a></figcaption></figure>')


def work_card(w):
    full = f'<small>{e(w["fullname"])}</small>' if w.get("fullname") else ""
    follow = f'<span class="follow">{e(u("follow"))}</span>' if w["group"] == "onegs" else ""
    links = "".join(f'<a href="{e(href)}" target="_blank" rel="noopener">{e(t(C.LINK[k]))}</a>' for k, href in w["links"])
    nums = "".join(f"<li>{e(t(n))}</li>" for n in w["nums"])
    return f'''
<article class="work" id="w-{w["id"]}" data-g="{w["group"]}">
  <div class="plate"><h3>{e(w["name"])}{full}</h3><span class="venue">{e(t(w["venue"]))}</span></div>
  <p class="org"><span>{e(t(w["org"]))}</span>{follow}</p>
  {media(w)}
  <div class="body">
    <p class="one">{e(t(w["one"]))}</p>
    <dl class="explain">
      <dt>{e(u("analogy"))}</dt><dd>{e(t(w["analogy"]))}</dd>
      <dt class="ins">{e(u("inspect"))}</dt><dd>{e(t(w["inspect"]))}</dd>
    </dl>
    <ul class="nums" aria-label="{e(u("nums_label"))}">{nums}</ul>
    <p class="links">{links}</p>
  </div>
</article>'''


def works():
    counts = {g: sum(1 for w in C.WORKS if w["group"] == g) for g, _ in C.GROUPS}
    filt = [f'<button type="button" class="filter" data-g="all" aria-pressed="true">{e(u("all"))} <span class="c">{len(C.WORKS)}</span></button>']
    for g, name in C.GROUPS:
        filt.append(f'<button type="button" class="filter" data-g="{g}" aria-pressed="false">{e(t(name))} <span class="c">{counts[g]}</span></button>')
    return f'''
<section class="station wrap" id="s2" aria-labelledby="s2-h">
  {section_head(2, "s2", u("s2"), u("s2_sub"))}
  <div class="filters" role="group" aria-label="{e(u("filter_label"))}">{"".join(filt)}</div>
  <div class="works">{"".join(work_card(w) for w in C.WORKS)}</div>
</section>'''


def need_thumb(n):
    if n["crop"]:
        art = (f'<svg viewBox="{n["crop"]}" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
               f'<use href="#scene" width="1200" height="560"/></svg>')
    elif n["n"] == 7:
        art = (f'<svg viewBox="0 0 240 180" preserveAspectRatio="xMidYMid meet" aria-hidden="true">'
               f'<path d="M0 162 H240" class="sc-floor-edge"/>'
               f'{stand(48, 162, 0.40)}{stand(120, 162, 0.50)}{stand(194, 162, 0.58)}</svg>')
    else:
        cells = "".join(f'<rect x="{20 + c * 13}" y="{40 + r * 10}" width="10" height="7" rx="1.5" class="gpu-cell"/>'
                        for r in range(8) for c in range(16))
        art = (f'<svg viewBox="0 0 240 180" aria-hidden="true">{cells}'
               f'<rect x="96" y="134" width="30" height="20" rx="3" class="gpu-one"/>'
               f'<text x="20" y="30" class="dia-t">{e(u("thumb_many"))}</text>'
               f'<text x="134" y="149" class="dia-t ink">{e(u("thumb_one"))}</text></svg>')
    return f'<div class="thumb">{art}<span class="pin">{n["n"]}</span></div>'


def needs():
    rows = []
    for n in C.NEEDS:
        if n["n"] == 7:
            rows.append(f'<p class="need-split">{e(u("need_split"))}</p>')
        rows.append(f'''
<div class="need" id="need-{n["n"]}">
  {need_thumb(n)}
  <div><h3>{e(t(n["title"]))}</h3><p class="desc">{e(t(n["desc"]))}</p></div>
  <dl>
    <div><dt>{e(u("need_ability"))}</dt><dd>{e(t(n["ability"]))}</dd></div>
    <div><dt>{e(u("need_works"))}</dt><dd class="chips">{"".join(wk(w) for w in n["works"])}</dd></div>
    <div><dt>{e(u("need_topics"))}</dt><dd class="chips">{"".join(tp(x) for x in n["topics"])}</dd></div>
  </dl>
</div>''')
    return f'''
<section class="station wrap" id="s3" aria-labelledby="s3-h">
  {section_head(3, "s3", u("s3"), u("s3_sub"))}
  <div class="needs">{"".join(rows)}</div>
</section>'''


def topics():
    choice_name = {k: t(v) for k, v in C.CHOICES}
    cards = []
    for tpc in C.TOPICS:
        bars = "".join(f'<span class="{"on" if i < tpc["level"] else ""}"></span>' for i in range(3))
        fit_labels = [choice_name[x] for x in tpc["tags"]]
        if LANG == "en":
            fit_labels = [s[0].lower() + s[1:] for s in fit_labels]
        fit = u("list_sep").join(fit_labels)
        month = "".join(f"<li>{e(t(m))}</li>" for m in tpc["month"])
        cards.append(f'''
<article class="topic" id="t-{tpc["id"]}" data-tags="{" ".join(tpc["tags"])}" data-letter="{tpc["id"].upper()}">
  <div class="t-head"><span class="t-letter" aria-hidden="true">{tpc["id"].upper()}</span>
    <h3>{e(t(tpc["title"]))}</h3>
    <span class="lvl"><i aria-hidden="true">{bars}</i>{e(u("level"))}{e(t(C.LEVELS[tpc["level"]]))}</span>
    <p class="sub">{e(t(tpc["sub"]))}</p></div>
  <div class="t-body">
    <p class="one">{e(t(tpc["one"]))}</p>
    <p class="fit">{e(u("fit"))}{e(fit)}</p>
    <dl>
      <div><dt>{e(u("t_problem"))}</dt><dd>{e(t(tpc["problem"]))}</dd></div>
      <div><dt>{e(u("t_read"))}</dt><dd class="chips">{"".join(wk(w) for w in tpc["read"])}</dd></div>
      <div><dt>{e(u("t_month"))}</dt><dd><ol>{month}</ol></dd></div>
      <div><dt>{e(u("t_output"))}</dt><dd>{e(t(tpc["output"]))}</dd></div>
    </dl>
  </div>
</article>''')
    choices = "".join(f'<button type="button" class="choice" data-tag="{k}" aria-pressed="false">{e(t(v))}</button>'
                      for k, v in C.CHOICES)
    return f'''
<section class="station wrap" id="s4" aria-labelledby="s4-h">
  {section_head(4, "s4", u("s4"), u("s4_sub"))}
  <div class="chooser"><p>{e(u("chooser_q"))}</p>
    <div class="choices">{choices}</div><p id="choice-out" aria-live="polite"></p></div>
  <div class="topics">{"".join(cards)}</div>
  <p class="onegs-note">{e(u("topics_note"))}</p>
</section>'''


def onboarding():
    weeks = "".join(
        f'<li class="week"><span class="w" aria-label="{e(u("week", n=i))}">W{i}</span><h3>{e(t(a))}</h3><p>{e(t(b))}</p></li>'
        for i, (a, b) in enumerate(C.WEEKS, 1))
    res = []
    for title, items in C.RESOURCES:
        lis = "".join(f'<li><a href="{e(href)}" target="_blank" rel="noopener">{e(t(n))}</a></li>' for n, href in items)
        tip = f'<p class="tip">{u("tip")}</p>' if title["en"] == "Run something first" else ""
        res.append(f'<div><h4>{e(t(title))}</h4><ul>{lis}</ul>{tip}</div>')
    gloss = []
    for term, zh_word, definition in C.GLOSSARY:
        extra = f'<span lang="zh-CN">{e(zh_word)}</span>' if LANG == "en" else ""
        gloss.append(f'<div><dt>{e(t(term))}{extra}</dt><dd>{e(t(definition))}</dd></div>')
    gsub = f'<p class="gloss-sub">{e(u("gloss_sub"))}</p>' if u("gloss_sub") else ""
    return f'''
<section class="station wrap" id="s5" aria-labelledby="s5-h">
  {section_head(5, "s5", u("s5"), u("s5_sub"))}
  <ol class="weeks">{weeks}</ol>
  <h3 class="sub-h">{e(u("res_h"))}</h3>
  <div class="res">{"".join(res)}</div>
  <h3 class="sub-h">{e(u("gloss_h"))}</h3>
  {gsub}
  <dl class="gloss">{"".join(gloss)}</dl>
</section>'''


def footer():
    src = "".join(
        f'<li><a href="{e(dict(w["links"])["paper"])}" target="_blank" rel="noopener">{e(w["name"])}</a>'
        f'{"：" if LANG == "zh" else ": "}{e(t(w["org"]))}{"，" if LANG == "zh" else ", "}{e(t(w["venue"]))}</li>'
        for w in C.WORKS)
    return f'''
<footer><div class="wrap">
  <h2>{e(u("footer_h"))}</h2><ol class="src">{src}</ol>
  <p>{e(u("footer_note"))}</p>
</div></footer>'''


def lang_switch():
    if LANG == "en":
        return '<div class="lang" role="group" aria-label="Language"><a href="zh/" hreflang="zh-CN" lang="zh-CN">中</a><span aria-current="true">EN</span></div>'
    return '<div class="lang" role="group" aria-label="语言"><span aria-current="true">中</span><a href="../" hreflang="en" lang="en">EN</a></div>'


def page(lang):
    global LANG
    LANG = lang
    out, html_lang, path = LANGS[lang]
    f = FONTS[lang]
    css = CSS.replace(":root{\n", f':root{{\n  --font:{f["font"]};--lh:{f["lh"]};--hls:{f["hls"]};\n', 1)
    nav = "".join(f'<a href="#s{i}">{e(t(x))}</a>' for i, x in enumerate(C.UI["nav"], 1))
    i18n = json.dumps({"out": u("choice_out"), "sep": u("list_sep")}, ensure_ascii=False)
    fav = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='14' "
           "fill='%23245BDF'/%3E%3Ccircle cx='16' cy='16' r='6' fill='%23fff'/%3E%3C/svg%3E")
    return f'''<!doctype html>
<html lang="{html_lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(u("title"))}</title>
<meta name="description" content="{e(u("desc"))}">
<meta property="og:title" content="{e(u("title"))}">
<meta property="og:description" content="{e(u("og_desc"))}">
<meta property="og:locale" content="{"en_US" if lang == "en" else "zh_CN"}">
<link rel="canonical" href="{SITE}{path}">
<link rel="alternate" hreflang="en" href="{SITE}">
<link rel="alternate" hreflang="zh-CN" href="{SITE}zh/">
<link rel="alternate" hreflang="x-default" href="{SITE}">
<link rel="icon" href="{fav}">
<style>{css}</style>
</head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>{S.scene_symbol()}</defs></svg>
<div class="bar"><div class="wrap"><a class="brand" href="#top">{e(u("brand"))}<span>{e(u("brand_sub"))}</span></a><nav class="nav" aria-label="{e(u("nav_label"))}">{nav}</nav>{lang_switch()}</div></div>
{hero()}
<main>
{primer()}
{works()}
{needs()}
{topics()}
{onboarding()}
</main>
{footer()}
<script>{JS.replace("__I18N__", i18n)}</script>
</body>
</html>'''


if __name__ == "__main__":
    for lang, (out, _, _) in LANGS.items():
        target = ROOT / out
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page(lang), encoding="utf-8")
        print(f"wrote {target.relative_to(ROOT)} ({target.stat().st_size / 1024:.1f} KB)")
