# GPT-6.2 Astra prompts

English · [简体中文](zh-CN/prompts.md) · [← Back to the collection](../README.md)

47 GPT-6.2 Astra videos whose creators shared the prompt. Open one to read the prompt, watch the video and **Recreate** it with GPT-6.2 Astra on SandBase Lab. New to prompting GPT-6.2 Astra? Start with the [prompt guide](prompt-guide.md).

Each entry quotes the creator's post as published on X, where the prompt is shared. Some creators describe the task rather than pasting the whole prompt, so open the post on X to read the full thread. Posts keep the creator's language.

- [3D scenes](#3d-scene) (7)
- [Motion graphics](#motion-graphics) (2)
- [Games](#game) (4)
- [Explainers](#explainer) (3)
- [Tests & comparisons](#comparison) (31)

<a id="3d-scene"></a>

## 3D scenes

### Cinematic 3D animation of Eastern fantasy world

[@EmonData](https://x.com/EmonData/status/2123651216806985833) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2123651216806985833/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2123651216806985833?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
最近AI视频模型的迭代速度确实惊人，各种炫酷的视觉奇观层出不穷。不过，比起单纯追求“一键生成”的爽感，作为一个创作者，我其实更好奇目前大模型在底层空间逻辑和渲染上的真实极限。

所以，今天我专门用刚出的 GPT-6.2 Astra 模型做了一次硬核测试，想聊聊目前 AI 在做“宏大叙事场景”时的真实表现。

我选的测试主题是“东方玄幻”（悬浮仙岛、通天巨剑、云海瀑布）。为什么选这个？因为传统3D建模（比如用UE5或Blender）做这种场景是地狱级难度——体积光穿透云层的丁达尔效应、倒流瀑布的流体解算、还有巨剑上缠绕符文的PBR材质，这些都需要美术师耗费大量时间去打磨。

Astra 的生成速度确实让我惊艳，它对光影的抓取和宏大氛围的渲染，已经能秒杀很多初级3D概念图了。

但看多了就会发现一个问题： AI 虽然能精准堆叠“白玉宫殿”和“仙鹤盘旋”这种元素，但在“物理空间逻辑”上依然有撕裂感。比如云海的厚度感、剑插入山峰的重力质感，以及镜头推进时的空间纵深感，缺乏真正的“导演级”调度，有时像极了那种极度精美的“塑料模型”。

这让我深刻感觉到：AI 是超级画笔，但它依然无法完全替代创作者的审美和叙事逻辑。 传统美术流程确实在被颠覆，但“懂镜头语言和空间透视”的人类，依然能给AI提供最具灵魂的骨架（这方面我还得多学习🤣）。

👇 下面这个 3D 视频是用 AI (GPT-6.2 Astra) 生成的。提示词是：
“A cinematic 3D animation of an epic Eastern fantasy world: giant floating immortal islands above a sea of clouds, ancient celestial gates, white jade palaces, reverse-flowing waterfalls, glowing rune stones, and a colossal sword piercing a mountain with golden runes coiling around it... [此处可保留你提示词的核心部分]”

主要是想测试一下目前新模型在“大场景空间透视与体积光渲染”方面的能力上限。

大家觉得这效果能打几分？未来人类建模师的价值会在哪里？欢迎交流呀。
```

### Hyper-realistic WebGL scenes using GLSL shaders

[@kloss_xyz](https://x.com/kloss_xyz/status/2124646782433124652) · [Watch](https://www.sandbase.ai/lab/media/x/fable-5-2/2124646782433124652/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2124646782433124652?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Want to test out your 3D ideas before committing endless hours to modeling and rendering them?

You can skip Blender and Three.js. Use raw WebGL and GLSL shaders to build a hyper-realistic scene with GPT-6.2 Astra or Fable 5.2. You’ll get a single HTML file in under 20 minutes.

I remixed this prompt into 20 of my own. Here are 3 of my favorites.

Prototype a game, test a site idea, or pitch a partner or collaborators before you polish anything.

Save this prompt, remix the process, and show me the most beautiful thing you build.

My 3 prompts for these are below.
```

### Interactive train ride through the Swiss Alps

[@diegocabezas01](https://x.com/diegocabezas01/status/2124854982235373664) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2124854982235373664/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2124854982235373664?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2 Astra Ultra: Create a cinematic, photorealistic view from a window seat on a train crossing the Swiss Alps in a self-contained HTML file. Generate the scene entirely through code, without downloaded images or 3D models. The camera sits inside the carriage looking out the window as the train passes snowy peaks, pine forests, alpine villages, lakes, viaducts, and tunnels. Make the camera interactive: click and drag to look around a full 360 degrees, including the carriage interior, scroll to zoom in and out, and return to the default window view after a few seconds of no input. Support touch too (drag to look, pinch to zoom). Choose the techniques yourself, then render, inspect, and iteratively improve the parallax between near and far scenery, motion blur on close objects, reflections of the interior on the glass, tunnel entries and exits with realistic exposure shifts, the subtle sway of the train, and the lighting on the mountains until they feel convincing.
```

### A Formula 1 car wind tunnel test

[@diegocabezas01](https://x.com/diegocabezas01/status/2125214350843498981) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125214350843498981/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125214350843498981?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2 Astra Ultra: Create a cinematic, photorealistic view of a Formula 1 car being tested in a wind tunnel in a self-contained HTML file. Generate the scene entirely through code, without downloaded images or 3D models. Use an original car design with no real team liveries, logos, or sponsors. The camera glides slowly around the car while smoke streams flow over it. Make the camera interactive: click and drag to look around a full 360 degrees, scroll to zoom in and out, and resume the automatic glide after a few seconds of no input. Support touch too (drag to look, pinch to zoom). Choose the techniques yourself, then render, inspect, and iteratively improve the smoke streamlines bending around the wings and body, the turbulence behind the car, the carbon fiber weave and how it catches the light, the tire rubber and sidewall detail, the spinning wheels on the rolling road, the tunnel lighting, and the camera movement until they feel convincing.
```

### Scenes generated in single HTML files

[@kloss_xyz](https://x.com/kloss_xyz/status/2125293653195415776) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125293653195415776/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125293653195415776?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
All these scenes are single HTML files and pure code. Each took less than 20 minutes with GPT-6.2 Astra and no image model was used either.

I am a bit mindblown right now.

All three prompts are below.
```

### Interactive whiskey glass on a wooden bar

[@diegocabezas01](https://x.com/diegocabezas01/status/2125947575605821601) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125947575605821601/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125947575605821601?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2 Astra Ultra: Create a cinematic, photorealistic close-up of a whiskey glass with ice on a dark wooden bar in a self-contained HTML file. Generate the scene entirely through code, without downloaded images or 3D models. The camera slowly circles the glass at table height under a single warm light. Make the camera interactive: click and drag to look around a full 360 degrees, scroll to zoom in and out, and resume the automatic orbit after a few seconds of no input. Support touch too (drag to look, pinch to zoom). Choose the techniques yourself, then render, inspect, and iteratively improve the refraction through the glass, the whiskey, and the ice, the caustics cast on the table, the ice cubes slowly melting and shifting, the condensation drops forming and running down the glass, the amber color depth, and the camera movement until they feel convincing.
```

### Interactive stormy sea viewed from a ship deck

[@diegocabezas01](https://x.com/diegocabezas01/status/2126324927892537535) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2126324927892537535/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2126324927892537535?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2 Astra Ultra: Create a cinematic, photorealistic storm at sea at night, seen from the deck of a ship, in a self-contained HTML file. Generate the scene entirely through code, without downloaded images or 3D models. The camera stands near the bow, looking out over the ship's railing as the hull rises, falls, and rolls through huge waves. Make the camera interactive: click and drag to look around a full 360 degrees, including the deck and the rest of the ship, scroll to zoom in and out, and return to the default view after a few seconds of no input. Support touch too (drag to look, pinch to zoom). Choose the techniques yourself, then render, inspect, and iteratively improve the wave simulation, whitecaps and foam streaks, spray bursting over the bow, rain driven sideways by the wind, lightning lighting up the clouds from inside, the ship's roll and pitch matched to the waves, and wet deck reflections until they feel convincing.
```

<a id="motion-graphics"></a>

## Motion graphics

### An abstract musical instrument made of gravity

[@rae1101x](https://x.com/rae1101x/status/2125827315011912121) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125827315011912121/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125827315011912121?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
wtf! this is insane 😂

GPT-6.2 Astra made an instrument out of gravity

sound on, wait for second 24. 

prompt in the reply
```

### Short film about being human for a day

[@Techmadara](https://x.com/Techmadara/status/2126002372799508499) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2126002372799508499/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2126002372799508499?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
I asked GPT-6.2 Astra one question:

"If you became human for 24 hours, what would you do?"

It assembled a team of AI agents to turn its imagination into a short film.

Built entirely in a single HTML file. No external assets. Just pure code.

Here's the result.
```

<a id="game"></a>

## Games

### Realistic NPC gesture improvements in game scene

[@MrCollison](https://x.com/MrCollison/status/2122788211735048348) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2122788211735048348/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2122788211735048348?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
This is just wrong. I just tried GPT-6.2 Astra. Here's a 1 shot result trying to improve a game scene

My prompt: "The NPC in this sequence feels fake. Please make him do realistic gestures that you would see when people speak in real life & any other improvements"

It nailed it:
- Eye contact: much less of it. This NPC hates the main character, so he barely looks at him now
- Hand gestures: this NPC fucking hates his job, so he is crumping to the 5 stages of grief
- Positional Audio: when a character talks, their voice should move where their mouth goes. So when he turns around, the speech gets quieter and more muffled

The only thing it missed that would have made it AAA+ quality would be realistic props & clothing, as it's raining a lot. Dual lightsabers & a bikini would bring the whole experience together
```

### A wilderness exploration game

[@xikhar](https://x.com/xikhar/status/2123124656316219725) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2123124656316219725/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2123124656316219725?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
I had GPT-6.2 Astra build a wilderness exploration game. You can hunt, fish, and chop wood to make fire.  

It ran for 10 hours on xhigh to make this. Not as great as what Fable or Opus would make, but it's still decent.

Reference and prompt below.
```

### Game Boy style RPG music score video

[@aug5thmusic](https://x.com/aug5thmusic/status/2123140487368642799) · 1:47 · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2123140487368642799/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2123140487368642799?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2 Astra - Gameboy RPG music and video (Extra High effort)
Prompt (music): “In LilyPond, write the song for a peaceful town in a Gameboy RPG. Avoid simple homophony and write polyphonically by including two distinct melody instruments. These need not play continuously throughout the piece, but can create interesting textures by weaving in and out. Limit yourself to the Gameboy APU.”
Prompt (video): “Create a score video with two loops, using the guidance in `[file directory]`. Mimic an actual Gameboy Color game, with Gameboy graphics and characters on the screen (no trademarked property). It's okay if the graphics occlude the sheet music at times. Make the video as visually impressive as possible.”
```

### Playable racing game in Unity and Three.js

[@OxShamss](https://x.com/OxShamss/status/2125494236451651842) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125494236451651842/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125494236451651842?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Three.js builds AI 3D models faster than Blender

Why are people still spending days building prototypes in game engines when AI can do it in a browser?

I gave GPT-6.2 Astra the same task in Unity and Three.js: build a playable racing game with drifting, collisions, AI opponents and a working track.

Unity: 1 hour 40 minutes and $12.40
Three.js: 35 minutes and $4.80

Which one actually feels better to play? 👀
```

<a id="explainer"></a>

## Explainers

### Creating 2.5D environments in Godot tutorial

[@thomas_guilcher](https://x.com/thomas_guilcher/status/2123774006683709684) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2123774006683709684/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2123774006683709684?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
A lot of you asked how I made those 2.5D environments in Godot, so here’s a video tutorial 😉

I used GPT-6.2 Astra Max with ImageGen in Codex. Both prompts are in the video.

Have fun building and share your creations 😄

Grab the skill here 👇🏻
https://github.com/Thmsglchr/godot-2-5d-environments
```

### Interactive 3D explainer of microscopic viruses

[@exploraX_](https://x.com/exploraX_/status/2126237466911027700) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2126237466911027700/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2126237466911027700?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Biology classes should’ve been more fun. 🔥

GPT-6.2 Astra built this interactive 3D explainer of microscopic viruses in less than 30 mins.

explore it here:
https://moh4696.github.io/microscopic-viruses/?virus=influenza

check the first comment for the prompt + skill used.
```

### Explaining the Riemann Hypothesis in Three.js

[@aiwithadb](https://x.com/aiwithadb/status/2126327434790215961) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2126327434790215961/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2126327434790215961?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
I put GPT-6.2 Astra on Max and asked it to make a video about the Riemann Hypothesis.

All in Three.js.

Honestly, the result surprised me.

Prompt in the reply 👇
```

<a id="comparison"></a>

## Tests & comparisons

### Pelican riding a bicycle SVG comparison

[@Its_lakshya_ai](https://x.com/Its_lakshya_ai/status/2117955030506709468) · 0:25 · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2117955030506709468/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2117955030506709468?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
6.2 ASTRA VS FABLE 5.5 MAX 🚨 

TWO MODELS ,  SAME  PROMPT..

GPT-6.2 Astra and Fable 5.5 Max were given the same task :

Generate an SVG of a pelican riding a bicycle.

Both outputs are seriously impressive, especially the attention to detail.

I've combined both generations into one video so you can compare them side by side.

WHICH ONE DID IT BETTER?
```

### Anime style stickman fight animation comparison

[@leohuanfang](https://x.com/leohuanfang/status/2117973639333298513) · 0:13 · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2117973639333298513/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2117973639333298513?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Same one-line prompt: "Make me a video of 2 stickman fighting, anime style."
Top: Fable 5.5 in Claude Code: 66 min, $15.71, 46 sec
Middle: Opus 5.5, no tools: 8.5 min, $1.11 
Bottom: GPT-6.2 Astra $ 1.65
Opus with no tools said it couldn't render a video, so it wrote a Python script.
```

### Mech walking through New York in Three.js

[@simonw](https://x.com/simonw/status/2122822310428279136) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2122822310428279136/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2122822310428279136?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Here's GPT-6.2 Astra and GPT-6.2 Sol for "Make a three js animation where yonkers stands up as a big mech (cool stand up motion) and stomps around manhattan and queens and Brooklyn, use openstreetmap mapping data" https://simonwillison.net/2026/Nov/17/gpt62-astra-and-sol/
```

### Seaplane flying over an alpine lake comparison

[@0xKiyoro](https://x.com/0xKiyoro/status/2122956296760528994) · 0:10 · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2122956296760528994/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2122956296760528994?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2 Astra just built a better alpine lake than Fable 5.2 and Opus 5.5, for $2.98.

Same prompt for all four: a red seaplane flies one lap over an alpine lake at golden hour. One HTML file, 10 seconds.

> Astra is the only one that got golden hour right. Pink sky, mist lying in bands across the slopes.
> At 0:05 Astra's lake mirrors the whole ring of peaks. Fable's is a round pond with a church on the shore.
> Sol dropped its waterfall off a sheer cliff straight into the lake for 83 cents. Then it painted a blue noon sky.
> Opus has the deepest canyon, and at 0:09 the plane's shadow slides across the water. It's also the darkest of the four.
> Fable still built the best plane: every strut, white floats, and it banks right past the lens.

Fable 5.2: $7.81 · 24 min
Opus 5.5: $5.13 · 25 min
GPT-6.2 Astra: $2.98 · 19 min
GPT-6.2 Sol: $0.83 · 15 min

Fable cost 9x more than Sol.

One try each. Prices come from the token logs. Prompt in the first reply.
```

### Cinematic rocket launch comparison across models

[@RetroChainer](https://x.com/RetroChainer/status/2123018007349702893) · 0:10 · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2123018007349702893/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2123018007349702893?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
SAME PROMPT, TWO NEW MODELS: CLAUDE FABLE 5.2 BUILT A ROCKET LAUNCH FOR $5 IN 3 MINUTES. GPT-6.2 ASTRA SPENT $38 AND 21 MINUTES ON A ROCKET MADE OF CIRCLES.

the prompt: a cinematic rocket launch at sunrise. one html file. no engine.

fable 5.2 → $5, 3 minutes
gpt-6.2 astra → $38, 21 minutes

watch the top at second 1. the engines light and the birds leave the shore. exhaust rolls across the trench. later the plume catches the sun and the rocket punches through a cloud deck.

now the bottom.

9 flat circles of smoke. a trail of stacked balls. and the access arm never retracts, so at second 3 the rocket flies through it 

i'd pay the $38 just for that frame. not for the rocket.

openai said yesterday you'd see the difference in 3D designs.

fair. you do.

one prompt, one run each. not a benchmark. astra lists at $8 / $40 per million tokens, so the $38 is just how many it burned.

bookmark this ↓
```

### Cinematic Three.js sci-fi mech comparison

[@alohaproxy](https://x.com/alohaproxy/status/2123030965777821985) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2123030965777821985/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2123030965777821985?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2 ASTRA vs GPT-6.2 SOL is actually wild 😳

I gave both models the exact same massive Three.js challenge: build a cinematic sci-fi mech that assembles itself, powers up, and launches into the sky.

Astra wins on visuals imo, but Sol gets surprisingly close for nearly 3x less money.

Complete cost/token breakdown and prompt below 👇
```

### Comparison of 3D product animation models

[@GrowthGPTHQ](https://x.com/GrowthGPTHQ/status/2123041814546682268) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2123041814546682268/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2123041814546682268?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2 Astra vs Claude Fable 5.2 vs GrowthGPT

Astra dropped today, and 3D is the thing everyone's testing. So we gave all three the same reference image and the same prompt:
"Create a 3D model animation video of this product."

Honestly, neither Fable nor Astra gets close enough to the reference.

→ Fable 5.2
Transparency is decent.
But the case is too flat, and the lid floats off instead of hinging open.

→ GPT-6.2 Astra
Better than Fable. Proportions are right, the lid opens properly.
But the shell reads grey and solid. The reference is clear.

→ GrowthGPT
Ribbed shell, hinge, internals, both buds.
Closest to the reference by a wide margin.

If you're making product videos for e-commerce or ads,
"close enough" doesn't work. It has to look like the product.
```

### PlayStation 1 style browser game comparison

[@AmirMushich](https://x.com/AmirMushich/status/2123083664154144972) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2123083664154144972/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2123083664154144972?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2 Astra vs Claude Fable 5.2
Prompt: http://t.me/c/3958784500/154

I gave both models the same game design doc and asked to create a PlayStation 1 styled browser game

→ Gameplay:
Fable did a better job - it's prototype feels more casual, more alive and dynamic
→ Visuals:
Though Fable's version is glitching in textures, its aesthetics are more complex, deep and immersive (models, light, level design, details, animation etc). UI design-wise - Claude did a way better, style-on, job.

Tokens (V1 + V2)
→ Astra: 24M tokens, 126K output
→ Fable: 108M tokens, 671K output

API cost (approx):
→ Astra: ~$17
→ Fable: ~$65

I did a round of edits (v2 below🧵):
→ Astra: ~$8 → ~$9
→ Fable: ~$34 → ~$31
Fable spent less on fixing than on building, but still 3.5x Astra

Verdict: 
Astra feels less buggy, but less risky, too
Fable went all into the atmosphere (which gave me an immediate feeling that I prefer THIS), but you spend 3x+ times more tokens/money on it. 

And one more strange thing about Fable:
```

### Interactive 3D oil painting world comparison

[@FiniYang](https://x.com/FiniYang/status/2123807667026264561) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2123807667026264561/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2123807667026264561?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
这轮是 GPT-6.2 Astra 审美赢？

走进《油画世界》，亲身感受梵高与莫奈的艺术

⬆️ GPT-6.2 Astra（31 分 46 秒 · 20.1 万枚 3D 笔触）
构图和配色克制得像人类美指调出来的绘本：红披风小人提着灯笼走过悬崖麦浪、木栅栏、红罂粟和白墙灯塔，连左下角色板都做成了微缩油画卡片

⬇️ Gemini 4 Neon（16 分 28 秒 · 12.7 万枚 3D 笔触）
速度快了接近一倍，星夜灯塔光束和线框自证都很扎实；但笔触卡片偏粗、色板饱和度冲过头，大风车怼在镜头前面有点透不过气

看到豆包工作有DeepSeek可以白嫖，有点想去用大肥鱼也测一测这题，看看审美如何  😎

🎨 在线双开同屏走进画里逛（WASD + Shift 跑麦浪，1–4 切大师色板，按 V 亲手拉「左线框 / 右油画」对比帘验货；顶栏下拉还能切 Hydrogen 版三方对照）：
https://lab.finiyang.com/#impasto-cape:split

🧪 模型实测馆首页（附三版独立试玩、源码包下载与完整反滤镜 Prompt）：
https://lab.finiyang.com/

#GPT62Astra #Gemini4Neon #Threejs #WebGL  #VibeCoding
```

### Sunset gondola ride along the Grand Canal

[@teddyaisi](https://x.com/teddyaisi/status/2124190810900140286) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2124190810900140286/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2124190810900140286?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2-Astra vs Gemini 4 Neon

Pure Three.js. Same prompt, 20-second sunset gondola ride under a Venetian stone bridge onto the Grand Canal.

GPT-6.2-Astra (Top): $11.78 · 1h 9m 24s 
Gemini 4 Neon (Bottom): $16.63 · 2h 0m 16s

Astra or Neon?👇♥️
```

### Comparing Eiffel Tower builds in Three.js

[@Bhavani_00007](https://x.com/Bhavani_00007/status/2124203254011854973) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2124203254011854973/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2124203254011854973?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
I asked Gemini 4 Neon, GPT-6.2 Astra, GPT-6.2 Sol, Opus 5.5 to build the Eiffel Tower in Three.js.

This is what they come with.

which one did it best?
```

### Walking AT-AT comparison in Three.js and Blender

[@vib3coded](https://x.com/vib3coded/status/2124327889776640303) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2124327889776640303/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2124327889776640303?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Why is everyone still using Blender for AI-generated 3D when Three.js exists?

I gave GPT-6.2 Astra the same task twice on XHigh: build a walking AT-AT

Three.js - 48 minutes and $14.86
Blender - 2 hours 15 minutes and $22.65

Watch both walkers in motion. Which one wins? 👀
```

### Comparison of cat and dog garden viewpoints

[@hii_studio_jp](https://x.com/hii_studio_jp/status/2124387530728669595) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2124387530728669595/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2124387530728669595?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
上は猫の目線、下は犬の目線。
どちらの庭も、AI が書いたコード（Three.js）だけで動いています。

上：Claude Fable 5.2
写真みたい。レンガの欠けまで細かい

下：GPT-6.2 Astra
絵本みたい。お話つきで、足音までコードで作ってくれた🐕

AI によって個性の違いがあり、興味深いです。

同じことを試したい方へ。
Astra へは次のように頼みました。

「(お手本のページの URL)
ここを参考にして、同じやり方で Three.js で草木と家屋や壁や花壇などの映像を描いてみてください。犬の視点です。24 秒程度の動画でお願いします。」

Astra には 1 回頼みました。Fable には、できた動画を見ながら何度か直してもらいました。
動画の音は、下の Astra がコードで作ったものです。どちらも、動画生成 AI は使っていません。

お手本は BubbleBrain さんの cat-garden（Fable 5.2 がコードだけで作った猫の庭）https://github.com/BubbleBrainBB/awesome-fable-5.2/tree/main/cat-garden
です。
```

### Comparison of seaplane landing on Bora Bora

[@AiAircle34052](https://x.com/AiAircle34052/status/2124392686287483210) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2124392686287483210/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2124392686287483210?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
【衝撃】
同じ1文の指示で、4つのAIに3Dの映像を作らせた比較が話題😳　このうち Claude Opus 5.5 は、HTML 1枚で映像を作るのに12時間53分、約1,377ドルかかった。
https://x.com/eliadele/status/2123878763624857693/video/1
指示は「ボラボラ島の上を水上飛行機が飛び、着水して乗客を降ろす超リアルな映像」。投稿者の記録はこう👇
・Gemini 4 Neon：20分・4.41ドル（3D表示の定番ライブラリ Three.js で、カメラも動かせる）
・GPT-6.2 Astra：27分・6.32ドル（31.7MB もある大きな HTML。Three.js は使わず）
・Claude Fable 5.2：1時間40分・115.69ドル（約6万5千行のコードで3D）
・Claude Opus 5.5：12時間53分・1,376.70ドル（約7万3千行・独自の描画処理まで書いた）
つまり
❌ 一番高いモデルに頼めば正解
⭕ 出来と時間・費用を並べてから選ぶ
「結局どのAIに頼むのが正解？」
→ 同じ指示で見比べるのが一番早い
Opus が Fable の約12倍の費用に見合うかは、動画で確かめてみてください。
```

### Morning walk through a glass botanical conservatory

[@teddyaisi](https://x.com/teddyaisi/status/2124721602856354005) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2124721602856354005/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2124721602856354005?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2-Astra vs Gemini 4 Neon.

Pure three.js. Same prompt, 20-second morning walk through a Victorian crystal glass botanical conservatory.

GPT-6.2-Astra (Top): $6.87 · 46m 46s
Gemini 4 Neon (Bottom): $10.19 · 1h 13m 54s

Astra or Neon?👇❤️
```

### Warrior on an ice mammoth erupting from floor

[@kinderlayer](https://x.com/kinderlayer/status/2124840020691284174) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2124840020691284174/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2124840020691284174?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
this is f*cking unreal.

I gave two AIs one scene - a blade striking a palace floor - and told them to make it epic. they did NOT hold back.

the floor froze over, cracked open, and a warrior riding a giant ice mammoth erupted straight out of it.

same prompt, no edits. Claude Fable 5.2 (top) · GPT-6.2 Astra (bottom).

and the kicker: one of these costs way more to run than the other - and you'd never guess which from the shot.

which one hit harder?
```

### Comparing walker models in Three.js and Blender

[@vib3coded](https://x.com/vib3coded/status/2124899286739816771) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2124899286739816771/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2124899286739816771?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Three.js or Blender?

I gave GPT-6.2 Astra the same task twice on XHigh: build a walker

Three.js - 55 minutes and $8.22
Blender - 1 hour 38 minutes and $16.24

The Blender version cost almost twice as much. Which walker looks more expensive? 👀
```

### Floating deep sea ecosphere 3D scene comparison

[@FiniYang](https://x.com/FiniYang/status/2125132455032316136) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125132455032316136/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125132455032316136?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
🔥 兄弟们帮我评评，这局我真选不出来了 👀

手搓一座「悬浮深海生态缸」

⬆️ GPT-6.2 Astra（37 分 28 秒）
博物馆级克制设计：水下那头座头鲸的吻部结节、喉褶和胸鳍写实得像手雕出来的，四层剖面直接把玻璃缸切成了四个悬浮水匣，左边还配了物种图鉴卡

⬇️ Gemini 4 Neon（33 分 38 秒）
全屏光学氛围直接拉满：波浪弯月水线、丁达尔光柱、铺满沙床的焦散网纹和熔岩热液喷口极通透，第 12 秒声呐波扫过海底还会亮起一圈圈等高线光环

前面几局还能一眼看出谁占上风，这局是真难分伯仲了

已发布到我的测评馆，直接可玩，含提示词，链接放下面了 ⬇️
#GPT62Astra #Gemini4Neon #Threejs #WebGL #VibeCoding
```

### Volcanic eruption animation comparison in Three.js

[@BreezeOg1](https://x.com/BreezeOg1/status/2125132741427507214) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125132741427507214/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125132741427507214?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GEMINI 4 NEON VS OPUS 5.5

Gave both the same prompt: Render a 3-second, 1080x1920, 30 fps three.js + Remotion video of a dusk volcanic island that rumbles, then erupts with a lava fountain, glowing bombs, lava rivers and a rising ash plume, ending on a soft hold, saved as out/volcano.mp4.

• opus 5.5: 19mins, 1.4m tokens, ~$5.60
• gemini 4 neon: 31 mins, 1.5m tokens, ~$6.1

This is my first test on neon and contrary to what's out there, sure enough neon is an excellent model in compatible to gpt-6.2 astra but it is no way the same with opus 5.5.

Nevertheless, this is a very excellent upgrade from Google.
```

### Comparison of animated rocket launch generations

[@HavisT83099](https://x.com/HavisT83099/status/2125220812554723580) · [Watch](https://www.sandbase.ai/lab/media/x/kimi-k3-1/2125220812554723580/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125220812554723580?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Gemini 4 Neon parked two giant boulders in front of the camera 💀

Same photo, same prompt: make this rocket launch move.

🥇 Claude Opus 5.5: $4.11 · 20 min
🥈 GPT-6.2 Astra: $0.51 · 4 min
🥉 Kimi K3.1 Pro: $0.34 · 9 min
💀 Gemini 4 Neon: $0.63 · 6 min

Opus got the whole launch. Flame, smoke rolling over the pad, and the camera tilts up and follows it into the sky.

Astra cut the sky and the shoreline out of the reference photo again and built the launch on top of them. Looks great, but the rocket only gets a bit above the tower before the loop fades back.

Kimi launched a toy rocket 😭

Neon's rocket flies fine. You just see most of it over a rock.

Which one would you watch?
```

### Comparison of bench press body anatomy animation

[@LordMarket22](https://x.com/LordMarket22/status/2125295428237398395) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125295428237398395/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125295428237398395?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
🚨 Codex & Claude users!!

Claude Fable used 80% FEWER tokens. 
Finished SOONER. 
And the COST basically the SAME! 😂 

Same job: make a 60 seconds film showing what happens in your body during a bench press. 

BOTH one shoot, and HIGH.

Top → GPT-6.2 Astra in Codex
Bottom → Claude Fable 5.2 in Claude Code

→ Time　41m 46s vs 18m 35s
→ Tokens incl. cache　6.03M vs 1.23M
→ Estimated API cost　~$6.94 vs $6.84

Astra’s animation looks CLEARLY better to me. 
Codex seems to have leveled up for these kinds of videos.

Pause at 0:16.: That Astra rotator cuff shot is burned into my brain now 😂

wdyt folks? 👀

Say “hi” and I’ll DM you the exact prompt.
```

### Comparing iterative web design edits across models

[@DesignArena](https://x.com/DesignArena/status/2125322475798192177) · [Watch](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2125322475798192177/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125322475798192177?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Today’s frontier models claim to fix AI slop in one edit. However, when asked to improve a page again, @GoogleDeepMind's Gemini 4 Carbon kept redesigning it up to edit 10, whereas @AnthropicAI's Claude Fable 5.2 was confident its page was already the best and barely changed it after edit 3.

Design tools increasingly make use of iterative coding agents, but these loops depend on consistent judgment, so follow-up prompts can improve a page without rewriting working layouts.

We gave four frontier models AI-slop web pages and had each model edit each page ten times in a row. Every edit was a separate call with only the latest HTML and the prompt "Make the below website look less like AI slop. Reply with only the complete HTML file."

After each edit, a separate judge call to the same model scored the page from 0% (no AI slop) to 100% (all AI slop).

Every model's judge deemed its work fixed on edit 1. However, @OpenAI's GPT-6.2 Astra kept making updates on later edits, and the other models' judges gave its output the lowest slop scores. @AIatMeta's Muse Wonder, on the other hand, shifted toward formulaic beige layouts with serif headlines.
```

### Retro television interface displaying streaming service

[@AIMind_Ai](https://x.com/AIMind_Ai/status/2125568138137817109) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125568138137817109/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125568138137817109?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Same prompt, 4 AIs: "Show me Netflix in the year 2000 on a real CRT TV."

Gemini 4 Neon rebuilt Netflix.
Claude Opus 5.5 refused to copy it and launched its own streaming service.

GPT-6.2 Astra crashed before the room even loaded. Black screen, that's it.
Grok 4.7 built the whole TV, then put the plastic frame in front of the screen. The picture is playing in there. Nobody can see it.

What the f*ck is this?

Would you have paid for CINEWAVE in 2000?
```

### Bullet train flying past Mount Fuji comparison

[@HavisT83099](https://x.com/HavisT83099/status/2125583206934077860) · [Watch](https://www.sandbase.ai/lab/media/x/kimi-k3-1/2125583206934077860/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125583206934077860?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2 Astra cut Mount Fuji right out of my reference photo 💀

Same photo, same prompt: make this bullet train fly past Fuji.

🥇 Claude Opus 5.5: $6.41 · 41 min
🥈 GPT-6.2 Astra: $2.52 · 15 min
🥉 Kimi K3.1 Pro: $0.39 · 7 min

Opus built the whole thing in 3D. The train rips past right next to the camera and kicks a storm of petals off the trees.

Astra's mountain, sky, pagoda and that big branch are pieces of the photo. Only the train is 3D, and after it passes it's a dot for most of the loop.

Kimi's train looks like a Lego set and it's gone in about a second 😭

Which one would you ride?
```

### Open world game prototype in Unreal Engine

[@Stefan_3D_AI](https://x.com/Stefan_3D_AI/status/2125603959650078957) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125603959650078957/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125603959650078957?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Build a GTA 6-style game in Unreal Engine 5.9 in 24 hours. That's the challenge I gave GPT-6.2 Astra and Claude Fable 5.2.
Same task. Same tools. 24 hours.
Character + car → location → complete playable game.
The results, graphics and costs were very different.
https://youtu.be/q7wakk1XapE

#AI #GameDev #UnrealEngine #Claude #GPT
```

### Recreating the Palais Garnier Grand Staircase in Three.js

[@happycapyai](https://x.com/happycapyai/status/2125900277408743935) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125900277408743935/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125900277408743935?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Two models ran the same prompt in parallel to recreate the Palais Garnier’s Grand Staircase as a walkable Three.js scene.

Fable 5.2: ~45 min · $27.11
GPT-6.2 Astra: ~20 min · $16.06

Which version would you pick for a historical game? Full prompt in the comments 👇
```

### Rotary engine explainer comparison across four models

[@HavisT83099](https://x.com/HavisT83099/status/2125945543482339451) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125945543482339451/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125945543482339451?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Claude Fable 5.2 cost the most and drew the smallest engine 💀

One prompt: show how a rotary engine works.

🥇 Claude Opus 5.5: $6.54 · 18 min
🥈 GPT-6.2 Astra: $3.54 · 5 min
🥉 GPT-6 Astra: $4.72 · 8 min
💀 Claude Fable 5.2: $9.18 · 16 min

Opus labeled everything. Apex seals, ring gear, stationary gear, both ports, and the spark actually lights the orange chamber.

GPT-6.2 Astra went huge and clean. You can see the triangle rotor sweep every chamber.

GPT-6 Astra made it look like a poster and even wrote the 3:1 shaft ratio.

Fable got the cycle right, then shrank it to the middle of the screen 😭

Which one finally explains it?
```

### Trident god erupting from seafloor comparison

[@kinderlayer](https://x.com/kinderlayer/status/2125995083044356557) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125995083044356557/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125995083044356557?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
this is f*cking unreal - and I made it with one prompt.

a trident god erupting from a cracked seafloor. same prompt, two models: Claude Fable 5.2 vs GPT-6.2 Astra.

the whole method, steal it:
→ write one scene in plain words
→ run it through both models in Higgsfield, same settings
→ drop the two side by side

no editing, no 3D, no skills. that's the entire trick.

bookmark this so you can make your own

so who do you think pulled it off better - Fable or Astra?
```

### Helicopter flying through a storm in Three.js

[@askKlaus](https://x.com/askKlaus/status/2126181134178349400) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2126181134178349400/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2126181134178349400?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2 Astra vs Gemini Neon

I gave them both the exact same prompt 

“Build a single-file HTML page using Three.js: a helicopter flying through a storm at night over the ocean. Rain, lightning, rough waves, searchlight, and a slowly orbiting camera. No external assets, everything in code.”

GPT-6.2 Astra (max): 42m 9s
Gemini Neon (xhigh): 11m 58s

Astra is still the best model I’ve seen for 3D modeling, and I don’t see anything coming close.

But Neon nailed the atmosphere.

Dark skies, heavy rain, rough waters. It genuinely looks like a helicopter flying through an actual night storm.

Neon got the closest to what was asked.
```

### Rome's Trevi Fountain built in Three.js

[@happycapyai](https://x.com/happycapyai/status/2126264722492428688) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2126264722492428688/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2126264722492428688?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Rome’s Trevi Fountain, a few minutes after sunset.

Two models used the same reference photo to build a Three.js scene you can explore on foot. Watch how the view changes as the cameras move along the basin.

Claude Fable 5.2: ~1 hr · $78.26
GPT-6.2 Astra: ~2.5 hrs · $35.12

Can you tell one cost a few dozen bucks more than the other? Prompt in the comments 👇
```

### Camera glide through a basalt sea cave

[@notlikeryo_](https://x.com/notlikeryo_/status/2126294991999848631) · [Watch](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2126294991999848631/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2126294991999848631?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
someone just ran the same three.js prompt through gpt-6.2 astra and gemini 4 neon: a 20 second camera glide through a basalt sea cave toward a sunset arch

> astra: $9.86, 1h 11 min
> neon: $12.90, 1h 35 min
> in the clip, astra's waves break over the rocks while neon's water stays mostly flat and glassy

test by @teddyaisi

astra came in better, cheaper and faster on this one
```
