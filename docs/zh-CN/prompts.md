# GPT-6.2 Astra 提示词

[English](../prompts.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

共 24 条 GPT-6.2 Astra 视频，作者公开了提示词。打开即可查看提示词、观看视频，并在 SandBase Lab 上用 GPT-6.2 Astra 一键 **复刻**。第一次写 GPT-6.2 Astra 提示词？先看 [提示词写法](prompt-guide.md)。

每条都按 X 上发布的原文引用作者帖子。有的作者描述的是任务而不是完整提示词，请打开 X 原帖查看完整讨论串。帖子原文保留作者语言。

- [3D 场景](#3d-scene) (4)
- [游戏](#game) (2)
- [讲解](#explainer) (1)
- [测试对比](#comparison) (17)

<a id="3d-scene"></a>

## 3D 场景

### 使用GLSL着色器构建的超逼真WebGL场景

[@kloss_xyz](https://x.com/kloss_xyz/status/2124646782433124652) · [观看](https://www.sandbase.ai/lab/media/x/fable-5-2/2124646782433124652/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2124646782433124652?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Want to test out your 3D ideas before committing endless hours to modeling and rendering them?

You can skip Blender and Three.js. Use raw WebGL and GLSL shaders to build a hyper-realistic scene with GPT-6.2 Astra or Fable 5.2. You’ll get a single HTML file in under 20 minutes.

I remixed this prompt into 20 of my own. Here are 3 of my favorites.

Prototype a game, test a site idea, or pitch a partner or collaborators before you polish anything.

Save this prompt, remix the process, and show me the most beautiful thing you build.

My 3 prompts for these are below.
```

### 穿越瑞士阿尔卑斯山的交互式列车视角

[@diegocabezas01](https://x.com/diegocabezas01/status/2124854982235373664) · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2124854982235373664/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2124854982235373664?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2 Astra Ultra: Create a cinematic, photorealistic view from a window seat on a train crossing the Swiss Alps in a self-contained HTML file. Generate the scene entirely through code, without downloaded images or 3D models. The camera sits inside the carriage looking out the window as the train passes snowy peaks, pine forests, alpine villages, lakes, viaducts, and tunnels. Make the camera interactive: click and drag to look around a full 360 degrees, including the carriage interior, scroll to zoom in and out, and return to the default window view after a few seconds of no input. Support touch too (drag to look, pinch to zoom). Choose the techniques yourself, then render, inspect, and iteratively improve the parallax between near and far scenery, motion blur on close objects, reflections of the interior on the glass, tunnel entries and exits with realistic exposure shifts, the subtle sway of the train, and the lighting on the mountains until they feel convincing.
```

### F1 赛车风洞空气动力学测试

[@diegocabezas01](https://x.com/diegocabezas01/status/2125214350843498981) · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125214350843498981/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125214350843498981?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2 Astra Ultra: Create a cinematic, photorealistic view of a Formula 1 car being tested in a wind tunnel in a self-contained HTML file. Generate the scene entirely through code, without downloaded images or 3D models. Use an original car design with no real team liveries, logos, or sponsors. The camera glides slowly around the car while smoke streams flow over it. Make the camera interactive: click and drag to look around a full 360 degrees, scroll to zoom in and out, and resume the automatic glide after a few seconds of no input. Support touch too (drag to look, pinch to zoom). Choose the techniques yourself, then render, inspect, and iteratively improve the smoke streamlines bending around the wings and body, the turbulence behind the car, the carbon fiber weave and how it catches the light, the tire rubber and sidewall detail, the spinning wheels on the rolling road, the tunnel lighting, and the camera movement until they feel convincing.
```

### 单 HTML 纯代码生成的 3D 场景

[@kloss_xyz](https://x.com/kloss_xyz/status/2125293653195415776) · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125293653195415776/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125293653195415776?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
All these scenes are single HTML files and pure code. Each took less than 20 minutes with GPT-6.2 Astra and no image model was used either.

I am a bit mindblown right now.

All three prompts are below.
```

<a id="game"></a>

## 游戏

### 游戏场景中的NPC逼真手势改进

[@MrCollison](https://x.com/MrCollison/status/2122788211735048348) · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2122788211735048348/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2122788211735048348?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
This is just wrong. I just tried GPT-6.2 Astra. Here's a 1 shot result trying to improve a game scene

My prompt: "The NPC in this sequence feels fake. Please make him do realistic gestures that you would see when people speak in real life & any other improvements"

It nailed it:
- Eye contact: much less of it. This NPC hates the main character, so he barely looks at him now
- Hand gestures: this NPC fucking hates his job, so he is crumping to the 5 stages of grief
- Positional Audio: when a character talks, their voice should move where their mouth goes. So when he turns around, the speech gets quieter and more muffled

The only thing it missed that would have made it AAA+ quality would be realistic props & clothing, as it's raining a lot. Dual lightsabers & a bikini would bring the whole experience together
```

### Game Boy风格RPG音乐与乐谱视频

[@aug5thmusic](https://x.com/aug5thmusic/status/2123140487368642799) · 1:47 · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2123140487368642799/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2123140487368642799?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2 Astra - Gameboy RPG music and video (Extra High effort)
Prompt (music): “In LilyPond, write the song for a peaceful town in a Gameboy RPG. Avoid simple homophony and write polyphonically by including two distinct melody instruments. These need not play continuously throughout the piece, but can create interesting textures by weaving in and out. Limit yourself to the Gameboy APU.”
Prompt (video): “Create a score video with two loops, using the guidance in `[file directory]`. Mimic an actual Gameboy Color game, with Gameboy graphics and characters on the screen (no trademarked property). It's okay if the graphics occlude the sheet music at times. Make the video as visually impressive as possible.”
```

<a id="explainer"></a>

## 讲解

### Godot制作2.5D游戏场景教程

[@thomas_guilcher](https://x.com/thomas_guilcher/status/2123774006683709684) · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2123774006683709684/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2123774006683709684?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
A lot of you asked how I made those 2.5D environments in Godot, so here’s a video tutorial 😉

I used GPT-6.2 Astra Max with ImageGen in Codex. Both prompts are in the video.

Have fun building and share your creations 😄

Grab the skill here 👇🏻
https://github.com/Thmsglchr/godot-2-5d-environments
```

<a id="comparison"></a>

## 测试对比

### 鹈鹕骑自行车的SVG动画对比

[@Its_lakshya_ai](https://x.com/Its_lakshya_ai/status/2117955030506709468) · 0:25 · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2117955030506709468/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2117955030506709468?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
6.2 ASTRA VS FABLE 5.5 MAX 🚨 

TWO MODELS ,  SAME  PROMPT..

GPT-6.2 Astra and Fable 5.5 Max were given the same task :

Generate an SVG of a pelican riding a bicycle.

Both outputs are seriously impressive, especially the attention to detail.

I've combined both generations into one video so you can compare them side by side.

WHICH ONE DID IT BETTER?
```

### 动漫风格火柴人打斗动画对比

[@leohuanfang](https://x.com/leohuanfang/status/2117973639333298513) · 0:13 · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2117973639333298513/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2117973639333298513?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Same one-line prompt: "Make me a video of 2 stickman fighting, anime style."
Top: Fable 5.5 in Claude Code: 66 min, $15.71, 46 sec
Middle: Opus 5.5, no tools: 8.5 min, $1.11 
Bottom: GPT-6.2 Astra $ 1.65
Opus with no tools said it couldn't render a video, so it wrote a Python script.
```

### Three.js 巨型机甲漫游纽约市动画

[@simonw](https://x.com/simonw/status/2122822310428279136) · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2122822310428279136/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2122822310428279136?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Here's GPT-6.2 Astra and GPT-6.2 Sol for "Make a three js animation where yonkers stands up as a big mech (cool stand up motion) and stomps around manhattan and queens and Brooklyn, use openstreetmap mapping data" https://simonwillison.net/2026/Nov/17/gpt62-astra-and-sol/
```

### 水上飞机掠过高山湖泊的多模型对比

[@0xKiyoro](https://x.com/0xKiyoro/status/2122956296760528994) · 0:10 · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2122956296760528994/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2122956296760528994?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

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

### 两款模型生成日出火箭发射对比

[@RetroChainer](https://x.com/RetroChainer/status/2123018007349702893) · 0:10 · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2123018007349702893/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2123018007349702893?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

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

### Three.js科幻机甲动画对比

[@alohaproxy](https://x.com/alohaproxy/status/2123030965777821985) · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2123030965777821985/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2123030965777821985?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2 ASTRA vs GPT-6.2 SOL is actually wild 😳

I gave both models the exact same massive Three.js challenge: build a cinematic sci-fi mech that assembles itself, powers up, and launches into the sky.

Astra wins on visuals imo, but Sol gets surprisingly close for nearly 3x less money.

Complete cost/token breakdown and prompt below 👇
```

### 多模型3D产品动画效果对比

[@GrowthGPTHQ](https://x.com/GrowthGPTHQ/status/2123041814546682268) · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2123041814546682268/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2123041814546682268?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

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

### 大运河上的日落贡多拉之旅

[@teddyaisi](https://x.com/teddyaisi/status/2124190810900140286) · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2124190810900140286/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2124190810900140286?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2-Astra vs Gemini 4 Neon

Pure Three.js. Same prompt, 20-second sunset gondola ride under a Venetian stone bridge onto the Grand Canal.

GPT-6.2-Astra (Top): $11.78 · 1h 9m 24s 
Gemini 4 Neon (Bottom): $16.63 · 2h 0m 16s

Astra or Neon?👇♥️
```

### Three.js 构建埃菲尔铁塔多模型对比

[@Bhavani_00007](https://x.com/Bhavani_00007/status/2124203254011854973) · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2124203254011854973/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2124203254011854973?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
I asked Gemini 4 Neon, GPT-6.2 Astra, GPT-6.2 Sol, Opus 5.5 to build the Eiffel Tower in Three.js.

This is what they come with.

which one did it best?
```

### Three.js与Blender行走AT-AT对比

[@vib3coded](https://x.com/vib3coded/status/2124327889776640303) · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2124327889776640303/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2124327889776640303?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Why is everyone still using Blender for AI-generated 3D when Three.js exists?

I gave GPT-6.2 Astra the same task twice on XHigh: build a walking AT-AT

Three.js - 48 minutes and $14.86
Blender - 2 hours 15 minutes and $22.65

Watch both walkers in motion. Which one wins? 👀
```

### 水晶玻璃植物温室中的清晨漫步

[@teddyaisi](https://x.com/teddyaisi/status/2124721602856354005) · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2124721602856354005/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2124721602856354005?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GPT-6.2-Astra vs Gemini 4 Neon.

Pure three.js. Same prompt, 20-second morning walk through a Victorian crystal glass botanical conservatory.

GPT-6.2-Astra (Top): $6.87 · 46m 46s
Gemini 4 Neon (Bottom): $10.19 · 1h 13m 54s

Astra or Neon?👇❤️
```

### Three.js 与 Blender 制作行走机器人对比

[@vib3coded](https://x.com/vib3coded/status/2124899286739816771) · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2124899286739816771/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2124899286739816771?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Three.js or Blender?

I gave GPT-6.2 Astra the same task twice on XHigh: build a walker

Three.js - 55 minutes and $8.22
Blender - 1 hour 38 minutes and $16.24

The Blender version cost almost twice as much. Which walker looks more expensive? 👀
```

### 悬浮深海生态缸 3D 场景对比

[@FiniYang](https://x.com/FiniYang/status/2125132455032316136) · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125132455032316136/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125132455032316136?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

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

### 火山喷发场景的AI生成对比

[@BreezeOg1](https://x.com/BreezeOg1/status/2125132741427507214) · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125132741427507214/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125132741427507214?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
GEMINI 4 NEON VS OPUS 5.5

Gave both the same prompt: Render a 3-second, 1080x1920, 30 fps three.js + Remotion video of a dusk volcanic island that rumbles, then erupts with a lava fountain, glowing bombs, lava rivers and a rising ash plume, ending on a soft hold, saved as out/volcano.mp4.

• opus 5.5: 19mins, 1.4m tokens, ~$5.60
• gemini 4 neon: 31 mins, 1.5m tokens, ~$6.1

This is my first test on neon and contrary to what's out there, sure enough neon is an excellent model in compatible to gpt-6.2 astra but it is no way the same with opus 5.5.

Nevertheless, this is a very excellent upgrade from Google.
```

### 四款模型生成火箭发射动态对比

[@HavisT83099](https://x.com/HavisT83099/status/2125220812554723580) · [观看](https://www.sandbase.ai/lab/media/x/kimi-k3-1/2125220812554723580/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125220812554723580?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

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

### 卧推过程身体肌肉机制动画对比

[@LordMarket22](https://x.com/LordMarket22/status/2125295428237398395) · [观看](https://www.sandbase.ai/lab/media/x/gpt-6-2-astra/2125295428237398395/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125295428237398395?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

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

### 多款模型迭代修改网页设计效果对比

[@DesignArena](https://x.com/DesignArena/status/2125322475798192177) · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2125322475798192177/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra/2125322475798192177?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra&utm_content=prompt-index)

```text
Today’s frontier models claim to fix AI slop in one edit. However, when asked to improve a page again, @GoogleDeepMind's Gemini 4 Carbon kept redesigning it up to edit 10, whereas @AnthropicAI's Claude Fable 5.2 was confident its page was already the best and barely changed it after edit 3.

Design tools increasingly make use of iterative coding agents, but these loops depend on consistent judgment, so follow-up prompts can improve a page without rewriting working layouts.

We gave four frontier models AI-slop web pages and had each model edit each page ten times in a row. Every edit was a separate call with only the latest HTML and the prompt "Make the below website look less like AI slop. Reply with only the complete HTML file."

After each edit, a separate judge call to the same model scored the page from 0% (no AI slop) to 100% (all AI slop).

Every model's judge deemed its work fixed on edit 1. However, @OpenAI's GPT-6.2 Astra kept making updates on later edits, and the other models' judges gave its output the lowest slop scores. @AIatMeta's Muse Wonder, on the other hand, shifted toward formulaic beige layouts with serif headlines.
```
