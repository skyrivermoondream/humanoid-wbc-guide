#!/usr/bin/env python3
"""Builds index.html for the humanoid whole-body-control topic guide."""
import html
import sys
from pathlib import Path

import content as C
import scene as S

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "index.html")
e = html.escape

CSS = r"""
:root{
  --bg:#F2F4F3;--surface:#FFFFFF;--surface-2:#E6EBE8;--ink:#16202A;--ink-2:#2F3B47;--muted:#56626E;
  --line:#CBD3D8;--line-strong:#97A3AD;--yellow:#F2B200;--yellow-soft:#FFF2C7;--yellow-ink:#6E5000;
  --green:#0B7A63;--green-soft:#DCEFE8;--orange:#C8460F;--blue:#275D90;--ochre:#9A6700;--slate:#4A5866;
  --wall:#E5EAE7;--floor:#D3DAD6;--steel:#8C99A5;--steel-dark:#56636F;--steel-light:#C4CDD3;--pipe:#8796A3;
  --cab:#B7C2CA;--cab-door:#CCD5DB;--water:#B7D2E6;--robot:#2B3A49;--robot-far:#98A5B0;--visor:#F2B200;--pack:#0B7A63;
  --screen:#0E151C;
  --font:"PingFang SC","HarmonyOS Sans SC","MiSans","Microsoft YaHei UI","Microsoft YaHei","Noto Sans SC","Noto Sans CJK SC","Source Han Sans SC",system-ui,sans-serif;
  --din:"DIN Alternate","DIN Condensed","Bahnschrift","Barlow Semi Condensed","Roboto Condensed","Arial Narrow",var(--font);
  color-scheme:light dark;
}
@media (prefers-color-scheme:dark){:root{
  --bg:#0F151B;--surface:#161E26;--surface-2:#1C2630;--ink:#E5EBEF;--ink-2:#C7D0D8;--muted:#98A4AF;
  --line:#2A3641;--line-strong:#4A5865;--yellow:#FFC229;--yellow-soft:#3A3010;--yellow-ink:#FFD979;
  --green:#3CC3A2;--green-soft:#12322B;--orange:#FF7C42;--blue:#82B4E6;--ochre:#E3AE45;--slate:#A7B4C1;
  --wall:#151F28;--floor:#1D2832;--steel:#6D7B88;--steel-dark:#8E9BA7;--steel-light:#384552;--pipe:#5D6B78;
  --cab:#2C3844;--cab-door:#35424E;--water:#26506F;--robot:#D4DDE4;--robot-far:#5C6A77;--visor:#FFC229;--pack:#3CC3A2;
  --screen:#060A0E;
}}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:64px}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.75 var(--font);-webkit-text-size-adjust:100%;overflow-x:clip}
a{color:var(--blue);text-underline-offset:3px;text-decoration-thickness:1px}
a:hover{text-decoration-thickness:2px}
:focus-visible{outline:3px solid var(--yellow);outline-offset:2px;border-radius:3px}
h1,h2,h3{line-height:1.3;margin:0;font-weight:800;letter-spacing:.01em}
p{margin:0}
.wrap{max-width:1120px;margin:0 auto;padding:0 24px}
@media (max-width:600px){.wrap{padding:0 16px}}
.din{font-family:var(--din)}

/* top bar: the walkway line with one stop per section */
.bar{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
.bar .wrap{display:flex;align-items:center;gap:20px;height:56px}
.bar{border-bottom:4px solid var(--yellow)}
.brand{font-weight:800;font-size:15px;color:var(--ink);text-decoration:none;white-space:nowrap}
.brand span{font-family:var(--din);color:var(--muted);font-weight:700;margin-left:6px}
.nav{margin-left:auto;display:flex;gap:2px;align-self:stretch}
.nav a{position:relative;display:flex;align-items:center;height:100%;padding:0 12px 4px;color:var(--muted);text-decoration:none;font-size:14px;white-space:nowrap}
.nav a::after{content:"";position:absolute;left:50%;bottom:-8.5px;width:9px;height:9px;margin-left:-4.5px;border-radius:50%;background:var(--bg);border:2px solid var(--line-strong)}
.nav a.on{color:var(--ink);font-weight:700}
.nav a.on::after{background:var(--yellow);border-color:var(--ink)}
@media (max-width:720px){.brand span{display:none}.bar .wrap{gap:8px}.nav a{padding:0 8px 4px}}
@media (max-width:360px){.brand{display:none}.nav{margin-left:0}}

/* hero */
.hero{padding-top:44px;padding-bottom:8px}
.hero-top{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:40px;align-items:end}
.hero h1{font-size:clamp(32px,5.2vw,54px);line-height:1.18;letter-spacing:0}
.hero h1 small{display:block;font-size:.62em;font-weight:700;color:var(--ink-2);margin-top:6px}
.lede{margin-top:18px;font-size:17px;color:var(--ink-2);max-width:34em}
.spec{background:var(--surface);border:1px solid var(--line);border-left:8px solid var(--yellow);padding:16px 20px;border-radius:4px}
.spec p{font-size:17px;line-height:1.7}
.spec b{font-weight:800}
.spec .meta{margin-top:10px;font-size:13px;color:var(--muted)}
@media (max-width:860px){.hero-top{grid-template-columns:1fr;gap:20px}}
.scene-box{margin-top:28px;border:1px solid var(--line);border-radius:6px;background:var(--wall);overflow-x:auto;overflow-y:hidden;-webkit-overflow-scrolling:touch}
.scene{display:block;width:100%;min-width:760px;height:auto}
.swipe{display:none;font-size:13px;color:var(--muted);margin-top:6px}
@media (max-width:760px){.swipe{display:block}}
.legend{list-style:none;padding:0;margin:14px 0 0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px 20px}
.legend a{display:flex;gap:10px;align-items:center;color:var(--ink);text-decoration:none;padding:4px 0;font-size:15px}
.legend a:hover span:last-child{text-decoration:underline}
@media (max-width:760px){.legend{grid-template-columns:1fr 1fr}}
@media (max-width:420px){.legend{grid-template-columns:1fr}}
.pin{flex:none;display:inline-grid;place-items:center;width:26px;height:26px;border-radius:50%;background:var(--yellow);border:2px solid var(--ink);color:#16202A;font:700 14px/1 var(--din)}

/* scene artwork */
.sc-wall{fill:var(--wall)}.sc-seam{stroke:var(--line);stroke-width:1.5}
.sc-ceiling{fill:var(--steel-dark)}.sc-tray{fill:none;stroke:var(--steel);stroke-width:2.5}.sc-tray-rib{stroke:var(--steel);stroke-width:2}
.sc-floor{fill:var(--floor)}.sc-floor-edge{stroke:var(--ink);stroke-width:2.5}.sc-lane{stroke:var(--yellow);stroke-width:3;stroke-dasharray:22 14;opacity:.75}
.sc-water{fill:var(--water)}.sc-water-glint{stroke:#fff;stroke-width:2.5;stroke-linecap:round;opacity:.85}
.sc-step{fill:var(--steel-light);stroke:var(--ink);stroke-width:1.5}.sc-grate{stroke:var(--steel-dark);stroke-width:2}.sc-step-edge{stroke:var(--yellow);stroke-width:5}
.sc-hanger{stroke:var(--steel-dark);stroke-width:4}.sc-pipe{fill:var(--pipe)}.sc-pipe-0{fill:var(--steel)}.sc-pipe-2{fill:var(--steel-dark)}.sc-clamp{fill:var(--steel-dark)}
.sc-hazard rect{fill:var(--yellow)}.sc-hazard-stripe{stroke:#16202A;stroke-width:3}
.sc-gauge-ring{fill:var(--steel-dark)}.sc-gauge-face{fill:#F7F9FA}.sc-needle{stroke:var(--orange);stroke-width:3;stroke-linecap:round}.sc-gauge-arc{fill:none;stroke:var(--green);stroke-width:3}
.sc-cabinet{fill:var(--cab);stroke:var(--ink);stroke-width:2}.sc-door{fill:var(--cab-door);stroke:var(--steel-dark);stroke-width:1.5}.sc-handle{fill:var(--ink)}
.sc-led-g{fill:var(--green)}.sc-led-y{fill:var(--yellow)}.sc-led-o{fill:var(--orange)}
.sc-warn{fill:var(--yellow);stroke:#16202A;stroke-width:2;stroke-linejoin:round}.sc-warn-bolt{fill:none;stroke:#16202A;stroke-width:2;stroke-linejoin:round}
.sc-vent{stroke:var(--steel-dark);stroke-width:2;opacity:.55}
.sc-booth-box{fill:var(--surface);stroke:var(--ink);stroke-width:2}.sc-screen{fill:var(--screen)}.sc-screen-line{fill:none;stroke:var(--green);stroke-width:2.5;stroke-linejoin:round}
.sc-op{fill:none;stroke:var(--ink);stroke-width:2.5}.sc-vr{fill:var(--yellow);stroke:#16202A;stroke-width:2}.sc-signal{fill:none;stroke:var(--blue);stroke-width:2.5;stroke-linecap:round}
.sc-link{fill:none;stroke:var(--blue);stroke-width:2.5;stroke-dasharray:7 8;stroke-linecap:round}
.sc-sight{stroke:var(--orange);stroke-width:2;stroke-dasharray:4 6}
.sc-leader{stroke:var(--ink);stroke-width:1.6}
.rb-near{stroke:var(--robot)}.rb-near-fill{fill:var(--robot)}.rb-far{stroke:var(--robot-far)}.rb-far-fill{fill:var(--robot-far)}
.rb-body{fill:var(--robot)}.rb-trim{stroke:var(--yellow)}.rb-visor{fill:var(--visor)}.rb-pack{fill:var(--pack)}
.rb-pack-line{fill:var(--bg);opacity:.45}.rb-led{fill:var(--yellow)}.rb-ant{stroke:var(--pack)}
.hero-route{fill:none;stroke:var(--yellow);stroke-width:9;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:0}
.sc-mark{cursor:pointer}
.sc-mark circle{fill:var(--yellow);stroke:#16202A;stroke-width:2.5;transition:transform .15s}
.sc-mark text{font:700 19px var(--din);fill:#16202A;text-anchor:middle;pointer-events:none}
.sc-mark circle,.sc-mark{transform-box:fill-box;transform-origin:center}
.sc-mark:hover circle,.sc-mark:focus-visible circle{transform:scale(1.15)}
@media (prefers-reduced-motion:no-preference){
  .hero-route{stroke-dashoffset:1;animation:walk 1.9s .25s cubic-bezier(.55,0,.25,1) forwards}
  .hero .sc-mark{animation:pop .5s calc(.55s + var(--i) * .2s) both}
}
@keyframes walk{to{stroke-dashoffset:0}}
@keyframes pop{from{opacity:0;transform:translateY(6px) scale(.5)}to{opacity:1;transform:none}}

/* sections */
.station{padding-top:72px;padding-bottom:8px}
.st-head{display:grid;grid-template-columns:auto 1fr;gap:4px 18px;align-items:center;margin-bottom:28px}
.st-no{position:relative;display:grid;place-items:center;width:52px;height:52px;border-radius:50%;background:var(--yellow);border:3px solid #16202A;color:#16202A;font:700 25px/1 var(--din)}
.st-no::before{content:"";position:absolute;right:100%;top:50%;margin-top:-4px;width:100vw;height:8px;background:var(--yellow);z-index:-1}
.st-head h2{font-size:clamp(25px,3.4vw,34px)}
.st-head p{grid-column:2;color:var(--muted);font-size:16px;max-width:42em}
@media (max-width:600px){.st-head{grid-template-columns:auto 1fr}.st-no{width:44px;height:44px;font-size:21px}.st-head p{grid-column:1 / -1}}
.sub-h{font-size:21px;margin:48px 0 6px}
.sub-p{color:var(--muted);max-width:44em;margin-bottom:22px}

/* pipeline */
.pipe{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:18px;position:relative}
.pipe::before{content:"";position:absolute;left:30px;right:30px;top:36px;height:4px;background:var(--line-strong)}
.stage{position:relative}
.stage .ic{position:relative;display:grid;place-items:center;width:72px;height:72px;border-radius:50%;background:var(--surface);border:2px solid var(--ink)}
.stage .ic .n{position:absolute;top:-6px;left:-6px;width:26px;height:26px;border-radius:50%;display:grid;place-items:center;background:var(--yellow);color:#16202A;border:2px solid #16202A;font:700 14px/1 var(--din)}
.ico{width:40px;height:40px;stroke:var(--ink);stroke-width:2.4}
.ico .i-dot{fill:var(--yellow);stroke:#16202A;stroke-width:1.4}.ico .i-thin{stroke-width:1.5;opacity:.7}.ico .i-dash{stroke-dasharray:3 3}
.stage h3{font-size:17px;margin-top:14px}
.stage .alias{justify-self:start;font-size:13px;color:var(--yellow-ink);background:var(--yellow-soft);display:inline-block;padding:0 8px;border-radius:3px;margin-top:4px}
.stage p{font-size:14.5px;color:var(--ink-2);margin-top:8px;line-height:1.7}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
.wk{display:inline-flex;align-items:center;gap:6px;font:700 13px/1 var(--din);padding:6px 9px;border:1px solid var(--line-strong);border-radius:20px;color:var(--ink);text-decoration:none;background:var(--surface)}
.wk::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--gc,var(--slate))}
.wk:hover{border-color:var(--ink)}
@media (max-width:1000px){.pipe{grid-template-columns:repeat(3,minmax(0,1fr));row-gap:36px}.pipe::before{display:none}}
@media (max-width:620px){.pipe{grid-template-columns:1fr;row-gap:22px}
  .pipe::before{display:block;left:34px;right:auto;top:30px;bottom:30px;width:4px;height:auto}
  .stage{display:grid;grid-template-columns:72px 1fr;gap:0 16px}.stage .ic{grid-row:span 4}.stage h3{margin-top:4px}}
[data-g=onegs]{--gc:var(--green)}[data-g=base]{--gc:var(--blue)}[data-g=data]{--gc:var(--ochre)}[data-g=real]{--gc:var(--slate)}[data-g=tool]{--gc:var(--line-strong)}

/* the three lines ONE-G follows */
.trio{display:grid;grid-template-columns:1fr 40px 1.15fr 40px 1fr;align-items:stretch;gap:0}
.leg{background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:18px 20px 20px;display:flex;flex-direction:column}
.leg.core{border:2px solid var(--green)}
.leg .role{font-size:13px;color:var(--muted)}
.leg h3{font:700 24px/1.2 var(--din);margin:2px 0 4px}
.leg .what{font-weight:700;font-size:16px}
.leg p{font-size:14.5px;color:var(--ink-2);margin-top:8px}
.leg svg{display:block;width:100%;height:auto;margin:12px 0 4px}
.arrow{display:grid;place-items:center;color:var(--ink)}
.arrow svg{width:32px;height:32px}
.gpu-cell{fill:var(--line-strong)}.gpu-one{fill:var(--yellow);stroke:#16202A;stroke-width:1.5}
.dia-t{font:700 13px var(--din);fill:var(--muted)}.dia-t.ink{fill:var(--ink)}
.lora{fill:var(--yellow);stroke:#16202A;stroke-width:1.5}.dia-arrow{fill:none;stroke:var(--ink);stroke-width:2.5;stroke-linecap:round;stroke-linejoin:round}
.in-chip{fill:var(--surface-2);stroke:var(--line-strong)}
.trio-note{margin-top:18px;padding:14px 18px;background:var(--green-soft);border-radius:4px;color:var(--ink);max-width:56em}
@media (max-width:900px){.trio{grid-template-columns:1fr;gap:0}.arrow{height:40px}.arrow svg{transform:rotate(90deg)}}

/* works */
.filters{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:22px}
.filter{font:inherit;font-size:14px;cursor:pointer;display:inline-flex;align-items:center;gap:8px;padding:7px 14px;border-radius:22px;border:1px solid var(--line-strong);background:var(--surface);color:var(--ink)}
.filter::before{content:"";width:9px;height:9px;border-radius:50%;background:var(--gc,var(--ink))}
.filter[data-g=all]::before{display:none}
.filter .c{font-family:var(--din);color:var(--muted)}
.filter[aria-pressed=true]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.filter[aria-pressed=true] .c{color:inherit;opacity:.7}
.works{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;align-items:start}
@media (max-width:900px){.works{grid-template-columns:1fr}}
.work{background:var(--surface);border:1px solid var(--line);border-radius:6px;overflow:hidden;scroll-margin-top:72px}
.work[hidden]{display:none}
.plate{display:flex;align-items:center;gap:12px;padding:12px 16px 12px 14px;border-left:8px solid var(--gc);background:var(--surface-2)}
.plate h3{font:700 25px/1.1 var(--din);letter-spacing:.01em}
.plate h3 small{font-size:14px;font-weight:700;color:var(--muted);margin-left:8px}
.plate .venue{margin-left:auto;font-size:12.5px;font-weight:700;padding:3px 9px;border-radius:3px;border:1px solid var(--line-strong);white-space:nowrap;color:var(--ink-2);background:var(--surface)}
.org{padding:8px 16px 0;font-size:13.5px;color:var(--muted);display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.follow{font-size:12.5px;font-weight:700;color:var(--green);border:1px solid var(--green);padding:0 8px;border-radius:3px}
.media{margin:12px 16px 0}
.screen{position:relative;aspect-ratio:16/9;background:var(--screen);border-radius:4px;overflow:hidden}
.screen video{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;background:var(--screen)}
.play{position:absolute;inset:0;margin:auto;width:max-content;height:max-content;display:flex;align-items:center;gap:10px;padding:10px 18px 10px 12px;border-radius:30px;border:2px solid #16202A;background:var(--yellow);color:#16202A;font:inherit;font-size:15px;font-weight:700;cursor:pointer}
.play svg{width:26px;height:26px}
.play:hover{transform:scale(1.04)}
.media.is-playing .play{display:none}
.fail{position:absolute;inset:0;display:none;place-content:center;text-align:center;padding:16px;color:#E5EBEF;font-size:14px;gap:8px}
.fail a{color:#FFD979}
.media.is-error .fail{display:grid}.media.is-error .play,.media.is-error video{display:none}
.clips{display:flex;gap:6px;margin-top:8px;overflow-x:auto;scrollbar-width:thin;padding-bottom:2px}
.clip{font:inherit;font-size:13px;white-space:nowrap;cursor:pointer;padding:4px 10px;border-radius:3px;border:1px solid var(--line);background:var(--surface);color:var(--ink-2)}
.clip[aria-selected=true]{background:var(--ink);border-color:var(--ink);color:var(--bg)}
.media figcaption{font-size:12px;color:var(--muted);margin-top:6px}
.media figcaption a{color:inherit}
.body{padding:14px 16px 18px}
.body .one{font-size:15.5px;line-height:1.75}
.explain{margin:12px 0 0;display:grid;gap:8px}
.explain div{display:grid;grid-template-columns:6.6em 1fr;gap:10px;font-size:14.5px;line-height:1.7}
.explain dt{font-weight:700;color:var(--muted);white-space:nowrap}
.explain dd{margin:0;color:var(--ink-2)}
.explain .ins dt{color:var(--green)}
@media (max-width:440px){.explain div{grid-template-columns:1fr;gap:0}}
.nums{list-style:none;padding:0;margin:14px 0 0;display:flex;flex-wrap:wrap;gap:6px}
.nums li{font:700 13px/1.2 var(--din);padding:5px 9px;border:1.5px solid var(--ink);border-radius:3px}
.links{margin-top:14px;display:flex;flex-wrap:wrap;gap:4px 16px;font-size:14px}
.work.flash{animation:flash 1.4s ease-out}
@keyframes flash{0%,30%{box-shadow:0 0 0 4px var(--yellow)}100%{box-shadow:0 0 0 0 transparent}}
.stack{position:absolute;inset:0;display:grid;align-content:center;gap:8px;padding:18px 22px}
.stack div{border:1.5px solid #E5EBEF;color:#E5EBEF;border-radius:4px;padding:8px 12px;font-size:14px;display:flex;justify-content:space-between;gap:10px}
.stack div b{font-family:var(--din)}
.stack div:nth-child(2){border-color:#FFC229}
.stack .cmd{border-style:dashed;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12.5px;color:#FFD979}

/* needs */
.needs{display:grid;gap:0;border-top:2px solid var(--ink)}
.need{display:grid;grid-template-columns:200px minmax(0,1fr) minmax(0,.95fr);gap:22px;padding:22px 0;border-bottom:1px solid var(--line);scroll-margin-top:72px}
.need .thumb{position:relative;border:1px solid var(--line);border-radius:4px;overflow:hidden;background:var(--wall);aspect-ratio:4/3}
.need .thumb svg{display:block;width:100%;height:100%}
.need .thumb .pin{position:absolute;left:8px;top:8px}
.need h3{font-size:19px}
.need .desc{color:var(--ink-2);margin-top:6px;font-size:15px}
.need dl{margin:0;display:grid;gap:10px;font-size:14.5px}
.need dt{font-size:13px;color:var(--muted);font-weight:700}
.need dd{margin:2px 0 0}
.tp{display:inline-flex;align-items:center;gap:6px;font-size:13.5px;font-weight:700;color:var(--ink);text-decoration:none;padding:4px 10px 4px 4px;border-radius:3px;background:var(--yellow-soft)}
.tp b{display:inline-grid;place-items:center;width:20px;height:20px;border-radius:2px;background:#16202A;color:#FFC229;font:700 12px/1 var(--din)}
.tp:hover{text-decoration:underline}
.need-split{margin:34px 0 0;font-size:15px;font-weight:800;color:var(--muted)}
@media (max-width:900px){.need{grid-template-columns:150px minmax(0,1fr)}.need dl{grid-column:1 / -1}}
@media (max-width:520px){.need{grid-template-columns:1fr}.need .thumb{max-width:260px}}

/* topics */
.chooser{background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:16px 18px;margin-bottom:22px}
.chooser p{font-weight:700}
.choices{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.choice{font:inherit;font-size:14.5px;cursor:pointer;padding:8px 14px;border-radius:4px;border:1.5px solid var(--ink);background:var(--surface);color:var(--ink)}
.choice[aria-pressed=true]{background:var(--yellow);color:#16202A;border-color:#16202A;font-weight:700}
#choice-out{margin-top:10px;font-size:14.5px;color:var(--ink-2);min-height:1.5em}
.topics{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}
@media (max-width:900px){.topics{grid-template-columns:1fr}}
.topic{background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:0 0 18px;transition:opacity .2s;scroll-margin-top:72px}
.topic.dim{opacity:.35}
.t-head{display:grid;grid-template-columns:auto 1fr auto;gap:2px 14px;align-items:center;padding:16px 18px 12px;border-bottom:1px dashed var(--line-strong)}
.t-letter{grid-row:span 2;display:grid;place-items:center;width:46px;height:46px;border-radius:4px;background:#16202A;color:#FFC229;font:700 24px/1 var(--din)}
.t-head h3{font-size:19px}
.t-head .sub{font-size:13.5px;color:var(--muted);grid-column:2}
.lvl{grid-row:span 2;text-align:right;font-size:12.5px;color:var(--muted);font-weight:700}
.lvl i{display:flex;gap:3px;justify-content:flex-end;margin-bottom:4px}
.lvl i span{width:14px;height:8px;border-radius:2px;background:var(--line)}
.lvl i span.on{background:var(--orange)}
.t-body{padding:14px 18px 0}
.t-body .one{font-size:15.5px}
.t-body dl{margin:12px 0 0;display:grid;gap:12px;font-size:14.5px}
.t-body dt{font-size:13px;color:var(--muted);font-weight:700}
.t-body dd{margin:3px 0 0;color:var(--ink-2)}
.t-body ol{margin:4px 0 0;padding-left:1.4em}
.t-body li{margin:2px 0}
.fit{font-size:13px;color:var(--muted);margin-top:4px}
.onegs-note{margin-top:20px;font-size:14.5px;color:var(--muted)}

/* first month */
.weeks{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:22px;position:relative}
.weeks::before{content:"";position:absolute;left:20px;right:20px;top:20px;height:4px;background:var(--yellow)}
.week .w{position:relative;display:grid;place-items:center;width:44px;height:44px;border-radius:50%;background:var(--surface);border:3px solid #16202A;font:700 15px/1 var(--din);color:var(--ink)}
.week h3{font-size:17px;margin-top:12px}
.week p{font-size:14.5px;color:var(--ink-2);margin-top:6px}
@media (max-width:860px){.weeks{grid-template-columns:1fr 1fr;row-gap:28px}.weeks::before{display:none}}
@media (max-width:520px){.weeks{grid-template-columns:1fr}}
.res{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;margin-top:8px}
.res h4{margin:0 0 6px;font-size:15px}
.res ul{margin:0;padding-left:1.1em;font-size:14.5px}
.res .tip{font-size:13px;color:var(--muted);margin-top:8px}
.res code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12.5px;background:var(--surface-2);padding:1px 5px;border-radius:3px}
@media (max-width:760px){.res{grid-template-columns:1fr}}
.gloss{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 28px;margin:0}
.gloss div{padding:10px 0;border-bottom:1px solid var(--line)}
.gloss dt{font-weight:800;font-size:15px}
.gloss dd{margin:2px 0 0;font-size:14.5px;color:var(--ink-2)}
@media (max-width:700px){.gloss{grid-template-columns:1fr}}

footer{margin-top:80px;border-top:4px solid var(--yellow);background:var(--surface);padding:28px 0 40px;font-size:13.5px;color:var(--muted)}
footer h2{font-size:15px;color:var(--ink);margin-bottom:8px}
.src{columns:2;column-gap:28px;padding-left:1.1em;margin:0 0 18px}
.src li{break-inside:avoid;margin:2px 0}
@media (max-width:700px){.src{columns:1}}
"""

JS = r"""
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // videos: show a first frame when near the viewport, play only on request
  function prime(fig) {
    const v = $('video', fig);
    if (!v || v.dataset.primed) return;
    v.dataset.primed = '1';
    const tab = $('.clip[aria-selected="true"]', fig) || $('.clip', fig);
    load(v, tab, false);
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
    const fig = v.closest('.media');
    fig.classList.add('is-playing');
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
    $$('.topic').forEach(t => {
      const hit = !tag || t.dataset.tags.split(' ').includes(tag);
      t.classList.toggle('dim', !hit);
      if (tag && hit) hits.push(t.dataset.letter);
    });
    out.textContent = tag ? '更适合你的课题：' + hits.join('、') + '（其余已变淡，再点一次恢复）' : '';
  }));

  // highlight the current stop in the top bar
  const links = $$('.nav a');
  if ('IntersectionObserver' in window) {
    const spy = new IntersectionObserver(es => es.forEach(en => {
      if (en.isIntersecting) links.forEach(a => a.classList.toggle('on', a.hash === '#' + en.target.id));
    }), { rootMargin: '-40% 0px -55% 0px' });
    links.forEach(a => { const s = document.querySelector(a.hash); if (s) spy.observe(s); });
  }
})();
"""

PLAY_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="11" fill="#16202A"/>'
            '<path d="M10 8 L16 12 L10 16 Z" fill="#FFC229"/></svg>')
ARROW_SVG = ('<svg viewBox="0 0 32 32" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.6" '
             'stroke-linecap="round" stroke-linejoin="round"><path d="M5 16 H26 M19 9 L26 16 L19 23"/></svg>')


STAND = dict(lean=0, near_leg=(8, 4), far_leg=(-8, -5), near_arm=(-8, 6), far_arm=(10, 20))


def stand(x, ground, scale, pose=None):
    """A standing robot whose feet touch `ground` after scaling about the pelvis."""
    pose = pose or STAND
    near, far = S.ankle_offsets(pose)
    ankle = max(near[1], far[1])
    return S.robot((x, ground - ankle * scale), pose, scale=scale)


def wk(wid):
    w = C.WORK[wid]
    return f'<a class="wk" data-g="{w["group"]}" href="#w-{wid}">{e(w["name"])}</a>'


def tp(tid):
    t = C.TOPIC[tid]
    return f'<a class="tp" href="#t-{tid}"><b>{tid.upper()}</b>{e(t["title"])}</a>'


def hero():
    labels = {n["n"]: n["title"] for n in C.NEEDS}
    legend = "".join(
        f'<li><a href="#need-{n}"><span class="pin">{n}</span><span>{e(labels[n])}</span></a></li>'
        for n in range(1, 7))
    return f'''
<header class="hero wrap" id="top">
  <div class="hero-top">
    <div>
      <h1>人形机器人全身运控<small>研究生课题地图</small></h1>
      <p class="lede">写给联合培养的研究生同学。先用五分钟看懂这个方向，再看 13 个前沿工作的视频和讲解，最后对照巡检现场，挑一个想做的课题。</p>
    </div>
    <div class="spec">
      <p><b>方向一句话：</b>以规模化运动跟踪模型作为人形机器人的通用“小脑”，围绕它做高效训练、跨本体迁移和真机落地。</p>
      <p class="meta">ONE-G（万机）整理，信息截至 2026 年 10 月。</p>
    </div>
  </div>
  <div class="scene-box">
    <svg class="scene" viewBox="0 0 1200 560" role="img" aria-labelledby="scene-title">
      <title id="scene-title">巡检现场示意：机器人沿巡检通道依次跨过湿滑台阶、蹲行通过低矮管架、跪姿读取低位仪表、伸手开配电柜门；背部背着检测设备；远处控制室可远程接管。</title>
      <use href="#scene" width="1200" height="560"/>
      {S.hero_overlay(labels)}
    </svg>
  </div>
  <p class="swipe">左右滑动看完整场景；点数字跳到对应的需求。</p>
  <ol class="legend" aria-label="巡检现场的六类需求">{legend}</ol>
</header>'''


def section_head(no, sid, title, sub):
    return (f'<div class="st-head"><span class="st-no" aria-hidden="true">{no}</span>'
            f'<h2 id="{sid}-h">{title}</h2><p>{sub}</p></div>')


def primer():
    stages = []
    for i, (ic, name, alias, desc, works) in enumerate(C.STAGES, 1):
        stages.append(
            f'<li class="stage"><div class="ic"><span class="n">{i}</span>{S.icon(ic)}</div>'
            f'<h3>{name}</h3><span class="alias">打个比方：{alias}</span><p>{desc}</p>'
            f'<div class="chips">{"".join(wk(w) for w in works)}</div></li>')

    # SuperMimic panel: 128 grey cells vs one highlighted cell
    cells = []
    for r in range(8):
        for c in range(16):
            cells.append(f'<rect x="{c * 15}" y="{r * 11}" width="12" height="8" rx="1.5" class="gpu-cell"/>')
    gpu = (f'<svg viewBox="0 0 300 110" aria-hidden="true"><g transform="translate(0 4)">{"".join(cells)}</g>'
           f'<text x="0" y="106" class="dia-t">SONIC：128 卡 × 7 天</text>'
           f'<rect x="262" y="36" width="24" height="16" rx="2" class="gpu-one"/>'
           f'<text x="296" y="106" class="dia-t ink" text-anchor="end">1 卡约 3 小时</text></svg>')
    # SONIC panel: one robot, several kinds of input
    sonic_robot = stand(168, 160, 0.55, dict(lean=2, near_arm=(-20, 10), far_arm=(18, 30), near_leg=(10, 4), far_leg=(-8, -6)))
    ins = ""
    for i, t in enumerate(("VR 遥操作", "人体视频", "VLA 指令", "规划器")):
        y = 18 + i * 34
        ins += (f'<rect x="0" y="{y}" width="92" height="24" rx="12" class="in-chip"/>'
                f'<text x="46" y="{y + 16.5}" class="dia-t ink" text-anchor="middle">{t}</text>'
                f'<path d="M96 {y + 12} C 116 {y + 12}, 112 80, 124 80" class="dia-arrow" stroke-width="1.6" opacity=".55"/>')
    sonic = (f'<svg viewBox="0 0 300 168" aria-hidden="true">{ins}'
             f'<path d="M126 80 h4" class="dia-arrow"/>{sonic_robot}'
             f'<text x="214" y="70" class="dia-t">同一个策略</text><text x="214" y="88" class="dia-t ink">稳稳做出来</text></svg>')
    # Any2Any panel: a short robot handing its skills to a taller one
    small = stand(62, 146, 0.42)
    tall = stand(232, 146, 0.55)
    a2a = (f'<svg viewBox="0 0 300 168" aria-hidden="true">{small}{tall}'
           f'<path d="M104 92 H172 M164 84 L173 92 L164 100" class="dia-arrow"/>'
           f'<rect x="120" y="104" width="38" height="20" rx="3" class="lora"/>'
           f'<text x="139" y="118.5" class="dia-t" text-anchor="middle" style="fill:#16202A">LoRA</text>'
           f'<text x="62" y="164" class="dia-t" text-anchor="middle">G1</text>'
           f'<text x="230" y="164" class="dia-t ink" text-anchor="middle">新本体</text></svg>')
    return f'''
<section class="station wrap" id="s1" aria-labelledby="s1-h">
  {section_head(1, "s1", "五分钟看懂这个方向", "人形机器人学动作，大致是一条六站的流水线。每一站都有代表性工作，点名字可以跳到下面的视频卡片。")}
  <ol class="pipe">{"".join(stages)}</ol>
  <h3 class="sub-h">ONE-G 正在跟进的三条线</h3>
  <p class="sub-p">三个工作分别解决三件事：底座够不够强，训练贵不贵，能不能装进自家机器人。</p>
  <div class="trio">
    <div class="leg"><span class="role">让训练更便宜</span><h3>SuperMimic</h3>{gpu}
      <p>用可微世界模型代替大部分仿真采样。按论文的对比，单卡约 3 小时就超过了 SONIC 发布版的回报。</p>
      <div class="chips">{wk("supermimic")}</div></div>
    <div class="arrow" aria-hidden="true">{ARROW_SVG}</div>
    <div class="leg core"><span class="role">通用跟踪底座</span><h3>SONIC</h3>{sonic}
      <p>一个大号的通用“小脑”：42M 参数、700 小时动捕，各种上层输入都交给同一个策略执行。</p>
      <div class="chips">{wk("sonic")}</div></div>
    <div class="arrow" aria-hidden="true">{ARROW_SVG}</div>
    <div class="leg"><span class="role">装进新身体</span><h3>Any2Any</h3>{a2a}
      <p>先做运动学对齐，再用 LoRA 只调动力学相关的部分，约 1% 的代价迁移到新本体。</p>
      <div class="chips">{wk("any2any")}</div></div>
  </div>
  <p class="trio-note">底座决定能力上限，SuperMimic 决定迭代速度，Any2Any 决定能不能落到自家机器人上。这三件事，正好是做巡检机器人最关心的。</p>
</section>'''


def media(w):
    if not w["clips"]:
        return ('<div class="media"><div class="screen"><div class="stack">'
                '<div><span>环境与任务</span><b>Isaac Lab 式 API</b></div>'
                '<div><span>GPU 并行物理</span><b>MuJoCo Warp</b></div>'
                '<div class="cmd">uvx --from mjlab --refresh demo</div>'
                '</div></div><figcaption>示意图：mjlab 的两层结构和官方给出的一行试跑命令。</figcaption></div>')
    tabs = []
    for i, (label, src, poster) in enumerate(w["clips"]):
        tabs.append(f'<button type="button" class="clip" role="tab" aria-selected="{"true" if i == 0 else "false"}" '
                    f'data-src="{e(src)}" data-poster="{e(poster or "")}" data-page="{e(w["page"])}">{e(label)}</button>')
    first = w["clips"][0]
    note = w.get("clip_note") or f'视频来自 {w["name"]} 官方项目页'
    if len(tabs) > 1:
        clips_row = f'<div class="clips" role="tablist" aria-label="{e(w["name"])} 视频片段">{"".join(tabs)}</div>'
    else:
        clips_row = tabs[0].replace('class="clip"', 'class="clip" hidden')
    poster = f' poster="{e(first[2])}"' if first[2] else ""
    return (f'<figure class="media"><div class="screen">'
            f'<video muted playsinline preload="none"{poster}></video>'
            f'<button type="button" class="play" aria-label="播放 {e(w["name"])} 视频">{PLAY_SVG}<span>播放视频</span></button>'
            f'<div class="fail"><span>这段视频暂时加载不了</span><a href="{e(w["page"])}" target="_blank" rel="noopener">去官方项目页观看</a></div>'
            f'</div>{clips_row}'
            f'<figcaption>{e(note)}，版权归原作者。<a href="{e(w["page"])}" target="_blank" rel="noopener">打开原页面</a></figcaption></figure>')


def work_card(w):
    full = f'<small>{e(w["fullname"])}</small>' if w.get("fullname") else ""
    follow = '<span class="follow">ONE-G 正在跟进</span>' if w["group"] == "onegs" else ""
    links = "".join(f'<a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a>' for t, u in w["links"])
    nums = "".join(f"<li>{e(n)}</li>" for n in w["nums"])
    return f'''
<article class="work" id="w-{w["id"]}" data-g="{w["group"]}">
  <div class="plate"><h3>{e(w["name"])}{full}</h3><span class="venue">{e(w["venue"])}</span></div>
  <p class="org"><span>{e(w["org"])}</span>{follow}</p>
  {media(w)}
  <div class="body">
    <p class="one">{e(w["one"])}</p>
    <dl class="explain">
      <div><dt>打个比方</dt><dd>{e(w["analogy"])}</dd></div>
      <div class="ins"><dt>和巡检的关系</dt><dd>{e(w["inspect"])}</dd></div>
    </dl>
    <ul class="nums" aria-label="关键数字">{nums}</ul>
    <p class="links">{links}</p>
  </div>
</article>'''


def works():
    counts = {g: sum(1 for w in C.WORKS if w["group"] == g) for g, _ in C.GROUPS}
    filt = [f'<button type="button" class="filter" data-g="all" aria-pressed="true">全部 <span class="c">{len(C.WORKS)}</span></button>']
    for g, name in C.GROUPS:
        filt.append(f'<button type="button" class="filter" data-g="{g}" aria-pressed="false">{name} <span class="c">{counts[g]}</span></button>')
    cards = "".join(work_card(w) for w in C.WORKS)
    return f'''
<section class="station wrap" id="s2" aria-labelledby="s2-h">
  {section_head(2, "s2", "13 个前沿工作，先看视频", "每张卡片：它做了什么、打个比方、和巡检有什么关系。视频都来自论文官方项目页，点“播放”才加载，下方小标签可以切换片段。")}
  <div class="filters" role="group" aria-label="按方向筛选">{"".join(filt)}</div>
  <div class="works" id="works-grid">{cards}</div>
</section>'''


def need_thumb(n):
    if n["crop"]:
        art = f'<svg viewBox="{n["crop"]}" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><use href="#scene" width="1200" height="560"/></svg>'
    elif n["n"] == 7:
        art = (f'<svg viewBox="0 0 240 180" preserveAspectRatio="xMidYMid meet" aria-hidden="true">'
               f'<path d="M0 162 H240" class="sc-floor-edge"/>'
               f'{stand(48, 162, 0.40)}{stand(120, 162, 0.50)}{stand(194, 162, 0.58)}</svg>')
    else:
        cells = "".join(f'<rect x="{20 + c * 13}" y="{40 + r * 10}" width="10" height="7" rx="1.5" class="gpu-cell"/>'
                        for r in range(8) for c in range(16))
        art = (f'<svg viewBox="0 0 240 180" aria-hidden="true">{cells}'
               f'<rect x="96" y="134" width="30" height="20" rx="2" class="gpu-one"/>'
               f'<text x="20" y="30" class="dia-t">128 卡 × 7 天</text><text x="134" y="149" class="dia-t ink">单卡</text></svg>')
    return f'<div class="thumb">{art}<span class="pin">{n["n"]}</span></div>'


def needs():
    rows = []
    for n in C.NEEDS:
        if n["n"] == 7:
            rows.append('<p class="need-split">研发侧还有两件事</p>')
        rows.append(f'''
<div class="need" id="need-{n["n"]}">
  {need_thumb(n)}
  <div><h3>{e(n["title"])}</h3><p class="desc">{e(n["desc"])}</p></div>
  <dl>
    <div><dt>需要的能力</dt><dd>{e(n["ability"])}</dd></div>
    <div><dt>可以参考</dt><dd class="chips">{"".join(wk(w) for w in n["works"])}</dd></div>
    <div><dt>对应课题</dt><dd class="chips">{"".join(tp(t) for t in n["topics"])}</dd></div>
  </dl>
</div>''')
    return f'''
<section class="station wrap" id="s3" aria-labelledby="s3-h">
  {section_head(3, "s3", "放到巡检现场看", "巡检是我们设想的落地场景之一。下面把现场的需求，逐条对到需要的能力、可参考的工作和对应课题。编号和页首插图里的数字一致。")}
  <div class="needs">{"".join(rows)}</div>
</section>'''


def topics():
    cards = []
    choice_name = dict(C.CHOICES)
    for t in C.TOPICS:
        bars = "".join(f'<span class="{"on" if i < t["level"] else ""}"></span>' for i in range(3))
        fit = "、".join(choice_name[x] for x in t["tags"])
        month = "".join(f"<li>{e(m)}</li>" for m in t["month"])
        cards.append(f'''
<article class="topic" id="t-{t["id"]}" data-tags="{" ".join(t["tags"])}" data-letter="{t["id"].upper()}">
  <div class="t-head"><span class="t-letter" aria-hidden="true">{t["id"].upper()}</span>
    <h3>{e(t["title"])}</h3>
    <span class="lvl"><i aria-hidden="true">{bars}</i>难度：{C.LEVELS[t["level"]]}</span>
    <p class="sub">{e(t["sub"])}</p></div>
  <div class="t-body">
    <p class="one">{e(t["one"])}</p>
    <p class="fit">适合喜欢：{fit}</p>
    <dl>
      <div><dt>要回答的问题</dt><dd>{e(t["problem"])}</dd></div>
      <div><dt>先读</dt><dd class="chips">{"".join(wk(w) for w in t["read"])}</dd></div>
      <div><dt>第一个月可以做</dt><dd><ol>{month}</ol></dd></div>
      <div><dt>可能的产出</dt><dd>{e(t["output"])}</dd></div>
    </dl>
  </div>
</article>''')
    choices = "".join(f'<button type="button" class="choice" data-tag="{k}" aria-pressed="false">{v}</button>' for k, v in C.CHOICES)
    return f'''
<section class="station wrap" id="s4" aria-labelledby="s4-h">
  {section_head(4, "s4", "6 个可选课题", "每个课题都写了要回答的问题、先读哪几篇、第一个月能做什么。难度只是相对参考，可以按兴趣调整。")}
  <div class="chooser"><p>你更喜欢做哪类事？点一下，适合的课题会留下来。</p>
    <div class="choices">{choices}</div><p id="choice-out" aria-live="polite"></p></div>
  <div class="topics">{"".join(cards)}</div>
  <p class="onegs-note">这些课题都可以结合 ONE-G 的巡检场景与机器人平台开展，具体安排以双方沟通为准。</p>
</section>'''


def onboarding():
    weeks = "".join(f'<li class="week"><span class="w">W{i}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>'
                    for i, (t, d) in enumerate(C.WEEKS, 1))
    res = []
    for title, items in C.RESOURCES:
        lis = "".join(f'<li><a href="{e(u)}" target="_blank" rel="noopener">{e(n)}</a></li>' for n, u in items)
        tip = ('<p class="tip">一行命令试跑：<code>uvx --from mjlab --refresh demo</code>。训练需要 NVIDIA GPU，macOS 只能做评估。</p>'
               if title == "先跑起来" else "")
        res.append(f'<div><h4>{e(title)}</h4><ul>{lis}</ul>{tip}</div>')
    gloss = "".join(f'<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in C.GLOSSARY)
    return f'''
<section class="station wrap" id="s5" aria-labelledby="s5-h">
  {section_head(5, "s5", "第一个月怎么上手", "不管最后选哪个课题，前四周都可以走同一条路：先跑通，再动手做数据，然后带着问题定方向。")}
  <ol class="weeks">{weeks}</ol>
  <h3 class="sub-h">资源</h3>
  <div class="res">{"".join(res)}</div>
  <h3 class="sub-h">术语表</h3>
  <dl class="gloss">{gloss}</dl>
</section>'''


def footer():
    src = "".join(
        f'<li><a href="{e(dict(w["links"])["论文"])}" target="_blank" rel="noopener">{e(w["name"])}</a>：{e(w["org"])}，{e(w["venue"])}</li>'
        for w in C.WORKS)
    return f'''
<footer><div class="wrap">
  <h2>论文来源</h2><ol class="src">{src}</ol>
  <p>页面里的视频都直接嵌入自各论文的官方项目页，版权归原作者所有。文字由 ONE-G（万机）整理，难免有疏漏，请以原论文为准。</p>
</div></footer>'''


def page():
    nav = "".join(f'<a href="#s{i}">{t}</a>' for i, t in enumerate(("看懂", "论文", "场景", "课题", "上手"), 1))
    fav = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='13' "
           "fill='%23F2B200' stroke='%2316202A' stroke-width='4'/%3E%3C/svg%3E")
    return f'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>人形机器人全身运控：研究生课题地图</title>
<meta name="description" content="13 个人形全身运控前沿工作的真机视频与通俗讲解，对照巡检场景给出 6 个可选研究生课题。ONE-G（万机）整理。">
<meta property="og:title" content="人形机器人全身运控：研究生课题地图">
<meta property="og:description" content="13 个前沿工作、巡检场景需求、6 个可选课题和第一个月上手路线。">
<link rel="icon" href="{fav}">
<style>{CSS}</style>
</head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>{S.scene_symbol()}</defs></svg>
<div class="bar"><div class="wrap"><a class="brand" href="#top">人形全身运控<span>课题地图</span></a><nav class="nav" aria-label="页面导航">{nav}</nav></div></div>
{hero()}
<main>
{primer()}
{works()}
{needs()}
{topics()}
{onboarding()}
</main>
{footer()}
<script>{JS}</script>
</body>
</html>'''


if __name__ == "__main__":
    OUT.write_text(page(), encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size / 1024:.1f} KB)")
