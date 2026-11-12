# GPT-6.2 Astra prompt guide: how to prompt GPT-6.2 Astra for video

English · [简体中文](zh-CN/prompt-guide.md) · [← Back to the collection](../README.md)

GPT-6.2 Astra doesn't output video. It writes code, and the creator records the page it writes. This guide is built from the prompts creators shared with their videos. The collection is young, so it has two patterns so far. It grows as more creators share prompts, and each example links to the post it came from.

## 1. Give one short task and name the deliverable

A single line is enough when the task is clear about what comes out. Two creators posted the same one-line brief to several models:

- "Generate an SVG of a pelican riding a bicycle." ([@Its_lakshya_ai](https://x.com/Its_lakshya_ai/status/2117955030506709468)): GPT-6.2 Astra and Fable 5.5 Max were given this one task, and the creator combined both outputs into one side-by-side video.
- "Make me a video of 2 stickman fighting, anime style." ([@leohuanfang](https://x.com/leohuanfang/status/2117973639333298513)): the same line went to Fable 5.5 in Claude Code, Opus 5.5 with no tools, and GPT-6.2 Astra.

The second post is a useful warning about the deliverable. Opus 5.5 with no tools said it couldn't render a video and wrote a Python script instead. Name the output you want in the prompt, such as a self-contained HTML page, so the result is something you can record.

## 2. Keep the same prompt across models

When you compare, change only the model. Both posts above put every model on the same wording, and the cost and time are then comparable. The creator's cost figures are in the [model comparison](model-comparison.md).

## A prompt to start from

```text
Build [subject] as ONE self-contained HTML file that opens directly from disk.

Look: [style, e.g. low-poly / cinematic / anime / neon], [mood, lighting, palette].
Motion: [what moves and how]. Autoplay a [10]-second sequence on load, then loop.
Interaction: [drag = …, scroll = …, click = …, keys = …].
Rules: [the numbers or constraints the scene must respect].

Technical:
- No external images, fonts, audio or models. Generate what you need in code.
- Fill the viewport, no scrolling.
- Before you finish, check that the page loads with zero console errors and that every control works.
- Return only the complete HTML, from <!DOCTYPE html> to </html>. Do not abbreviate.
```

Try it in the [Lab text arena](https://www.sandbase.ai/arena/text?models=openai%2Fgpt-6.2-astra&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra) against other models, or with the API in the [tutorial](tutorial.md).

---

Quotes are short excerpts credited to their authors; follow the links for the full posts and videos.
