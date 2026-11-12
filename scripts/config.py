"""Every model-specific value for this list. The other scripts are generic and read from here."""
import os

ORIGIN = os.environ.get('LAB_ORIGIN', 'https://www.sandbase.ai').rstrip('/')
SITE = 'https://www.sandbase.ai'  # public links in READMEs and docs always use the canonical host

SLUG = 'gpt-6-2-astra'
REPO = 'sandbase-lab/awesome-gpt-6-2-astra'

CFG = dict(
    slug=SLUG,
    kind='code',
    name='GPT-6.2 Astra',
    short='GPT-6.2 Astra',  # how the prose refers to the model after the first mention
    vendor='OpenAI',
    model_id='openai/gpt-6.2-astra',
    repo=REPO,
    repo_url=f'https://github.com/{REPO}',
    campaign='awesome-gpt-6-2-astra',
    lab_collection=f'{SITE}/lab/ai-videos/{SLUG}',
    lab_data=f'{ORIGIN}/lab/data/ai-videos/{SLUG}.json',
    media_prefix=f'{SITE}/lab/media/x/{SLUG}/',
    model_page=f'{SITE}/model/openai/gpt-6.2-astra',
    arena=f'{SITE}/arena/text?models=openai%2Fgpt-6.2-astra',
    evals=f'{SITE}/leaderboards',
    pelican=f'{SITE}/arena/pelican-test',
    keys=f'{SITE}/console/keys',
    sandbox=f'{SITE}/landing/sandbox',
    lab_home=f'{SITE}/lab/',
    all_collections=f'{SITE}/lab/ai-videos',
    user_agent=f'awesome-gpt-6-2-astra-sync/1.0 (+https://github.com/{REPO})',
    html_out='astra.html',
    # Output limit for the curl example. Set to leave room for a long single-file page.
    max_tokens=128000,
    # Left unset until `sandbase inspect openai/gpt-6.2-astra` resolves; the model was not listed when this list was built.
    max_tokens_limit=None,
    context_length=None,
    guide_patterns=2,  # numbered sections in docs/prompt-guide.md
    banner_title='Awesome GPT-6.2 Astra',
    banner_sub='Videos · prompts · tutorial · model comparison',
    # Finished pieces only on the banner: no comparisons or other models' names.
    banner_skip=('vs', 'versus', 'comparison', 'compar', 'benchmark', 'test', 'opus', 'claude', 'fable', 'sonnet',
                 'haiku', 'gpt', 'gemini', 'argon', 'deepseek', 'kimi', 'grok', 'qwen', 'glm'),
    not_affiliated={'en': 'Not affiliated with or endorsed by OpenAI.', 'zh-CN': '与 OpenAI 无隶属或背书关系。'},
    # No SandBase blog post on this model was in the sources this list was built from; build_readme.py
    # skips the reading section while this is empty. Do not invent links here.
    reading=[],
)

# README and prompt-index copy. Placeholders in {braces} are filled by build_readme.py
# ({name}, {short}, {model_id}, {html_out}, links such as {lab_stats} or {model_page}, counts {n}/{a}/{p}).
# Every fact here comes from the collection feed (31 posts, 2 with a shared prompt), the two creator
# posts linked in the FAQ, and the announcement date recorded for the collection.
COPY = {
    'en': {
        'switch': 'English · [简体中文](README.zh-CN.md)',
        'tagline': 'A curated list of **GPT-6.2 Astra examples**: videos, prompts and demos made with GPT-6.2 Astra, OpenAI\'s model announced on November 1, 2026. Three.js and WebGPU 3D scenes, motion graphics, product UI, games and explainers, each one credited to its creator and linked to the original post. The model writes code, and each video is a page recorded as it plays.',
        'alt': 'Awesome GPT-6.2 Astra: videos, prompts, tutorial and model comparison',
        'stats': '**{n} videos** from **{a} creators** · **{p}** with the creator\'s prompt · synced daily from [SandBase Lab]({lab_stats})',
        'start': 'Start here',
        'start_rows': [
            ('Watch the videos', '[Browse by category](#contents) below, or [play them full-size on SandBase Lab]({lab_quickstart})'),
            ('Copy a prompt', '[Prompt index](docs/prompts.md): every video that comes with its prompt'),
            ('Write your own prompt', '[Prompt guide](docs/prompt-guide.md): {guide_patterns} patterns and a fill-in template'),
            ('Make a video', '[Tutorial](docs/tutorial.md): prompt → HTML → MP4, with the API, the CLI and a recording script'),
            ('Pick a model', '[GPT-6.2 Astra vs. Fable 5.5 and Claude Opus 5.5](docs/model-comparison.md)'),
            ('Try it now', '[Run GPT-6.2 Astra in the Lab arena]({arena_quickstart}), next to other models'),
        ],
        'goal': 'I want to…', 'where': 'Go to',
        'how': 'Click a preview to play the video. Click a title for the post, the prompt and **Recreate** on SandBase Lab. **@handle** links to the creator\'s post on X.',
        'contents': 'Contents',
        'featured': 'Featured',
        'show_all': 'Show all {n}',
        'recreate': 'Recreate a video with {name}',
        'recreate_body': [
            'Every video page on [SandBase Lab]({lab_recreate}) has a **Recreate** button: it sends the post to {short} in the Lab text arena and returns the code, ready to play in the browser.',
            '',
            'With the API, {name} is `{model_id}` on SandBase (OpenAI-compatible). Put a prompt in `prompt.txt`, create a key in the [console]({keys}), and run:',
        ],
        'recreate_after': 'Open `{html_out}` in a browser, or run it in a [SandBase Sandbox]({sandbox}) to keep generated code isolated. The call above sets `max_tokens` to 128,000 so a long page is not cut off. Full walkthrough: [tutorial](docs/tutorial.md). Pricing: [model page]({model_page}).',
        'prompt_tag': 'prompt',
        'more': '**[See all {n} on SandBase Lab →]({lab_section})**',
        'faq': 'FAQ',
        'faq_items': [
            ('What is GPT-6.2 Astra?', 'GPT-6.2 Astra is an OpenAI model, announced on November 1, 2026. Creators in this collection ran it next to Claude Opus 5.5 and Fable 5.5. On SandBase its id is `{model_id}`.'),
            ('How are these GPT-6.2 Astra videos made?', 'The model doesn\'t render video. It writes a web page, and the creator records the page playing. See the [tutorial](docs/tutorial.md).'),
            ('Where do I find the prompt for a video?', 'Videos tagged **prompt** come with the creator\'s prompt on their Lab page. The [prompt index](docs/prompts.md) lists all of them.'),
            ('How do I write a good GPT-6.2 Astra prompt?', 'Name one self-contained HTML file and the renderer you want, describe the scene and the state a recording should catch, rule out external assets, and ask the model to test its own page. Details and a template: [prompt guide](docs/prompt-guide.md).'),
            ('How do I use the GPT-6.2 Astra API?', 'On SandBase the model id is `{model_id}` on the OpenAI-compatible `/v1/chat/completions` endpoint. See [Recreate](#recreate) and the [model page]({model_page}).'),
            ('Is GPT-6.2 Astra better than Fable 5.5 or Claude Opus 5.5?', 'So far the evidence is creator runs, and they point different ways. On one stickman-fight prompt, GPT-6.2 Astra cost $1.65, against $15.71 for Fable 5.5 in Claude Code and $1.11 for Opus 5.5 with no tools. On a pelican SVG shown side by side with Fable 5.5 Max, the creator called both outputs "seriously impressive" and asked viewers to pick. This list has no measured GPT-6.2 Astra result yet: its Evals and Pelican Test rows were not in the sources it was built from. Details: [model comparison](docs/model-comparison.md).'),
            ('How much does one video cost?', 'A creator reported $1.65 for one GPT-6.2 Astra run on the stickman prompt, next to $15.71 for Fable 5.5 and $1.11 for Opus 5.5 on the same prompt. These are single runs with each creator\'s own setup. For list price, see the [model page]({model_page}).'),
            ('Can I reuse these videos?', 'No, not by default. They belong to their creators. See [MEDIA-RIGHTS](MEDIA-RIGHTS.md).'),
        ],
        'contribute': 'Suggest a video',
        'contribute_body': 'Know a GPT-6.2 Astra creation that should be here? [Open a submission]({repo_url}/issues/new?template=submit-video.yml) with the original X post. Accepted posts are added on SandBase Lab and show up here on the next daily sync. If this list helped you, a ⭐ helps others find it.',
        'credits': 'Credits & rights',
        'credits_body': [
            'Every video, prompt and post belongs to its creator. Cards credit the author and link to the original post. The MIT license covers this repository\'s scripts only. To correct a credit or remove a video, see [MEDIA-RIGHTS](MEDIA-RIGHTS.md).',
            '{not_affiliated}',
        ],
        'footer': 'Maintained by [SandBase Lab]({lab_home}) · [All AI video collections]({all_collections})',
        'p_title': 'GPT-6.2 Astra prompts',
        'p_switch': 'English · [简体中文](zh-CN/prompts.md) · [← Back to the collection](../README.md)',
        'p_intro': '{n} GPT-6.2 Astra videos whose creators shared the prompt. Open one to read the prompt, watch the video and **Recreate** it with {short} on SandBase Lab. New to prompting {short}? Start with the [prompt guide](prompt-guide.md).',
        'p_note': 'Each entry quotes the creator\'s post as published on X, where the prompt is shared. Some creators describe the task rather than pasting the whole prompt, so open the post on X to read the full thread. Posts keep the creator\'s language.',
        'p_watch': 'Watch',
        'p_open': 'Recreate on SandBase Lab',
    },
    'zh-CN': {
        'switch': '[English](README.md) · 简体中文',
        'tagline': '精选 **GPT-6.2 Astra 案例**合集：用 GPT-6.2 Astra（OpenAI 模型，2026 年 11 月 1 日宣布）做出的视频、提示词和演示。包括 Three.js 与 WebGPU 3D 场景、动效、产品界面、游戏和讲解，均注明作者并链接原帖。模型写的是代码，每条视频都是页面播放时录下的画面。',
        'alt': 'Awesome GPT-6.2 Astra：视频、提示词、教程和模型对比',
        'stats': '共 **{n} 条视频**，来自 **{a} 位创作者** · **{p} 条**附作者提示词 · 每天从 [SandBase Lab]({lab_stats}) 同步',
        'start': '从这里开始',
        'start_rows': [
            ('看视频', '在下方 [按分类浏览](#contents)，或 [在 SandBase Lab 大屏播放]({lab_quickstart})'),
            ('复制提示词', '[提示词索引](docs/zh-CN/prompts.md)：所有附带提示词的视频'),
            ('自己写提示词', '[提示词写法](docs/zh-CN/prompt-guide.md)：{guide_patterns} 条写法和一个填空模板'),
            ('做一个视频', '[教程](docs/zh-CN/tutorial.md)：提示词 → HTML → MP4，含 API、CLI 调用和录屏脚本'),
            ('选模型', '[GPT-6.2 Astra 对比 Fable 5.5 和 Claude Opus 5.5](docs/zh-CN/model-comparison.md)'),
            ('马上试试', '[在 Lab 竞技场运行 GPT-6.2 Astra]({arena_quickstart})，和其他模型并排对比'),
        ],
        'goal': '我想…', 'where': '去这里',
        'how': '点击预览图播放视频；点击标题前往 SandBase Lab 查看原帖、提示词，并一键 **复刻**；**@作者** 链接到 X 原帖。',
        'contents': '目录',
        'featured': '精选',
        'show_all': '展开全部 {n} 条',
        'recreate': '用 {name} 复刻视频',
        'recreate_body': [
            '[SandBase Lab]({lab_recreate}) 的每个视频页都有 **复刻** 按钮：在 Lab 文本竞技场把帖子内容发给 {short}，返回可在浏览器直接播放的代码。',
            '',
            '用 API 的话，{name} 在 SandBase 上的模型 ID 是 `{model_id}`（兼容 OpenAI）。把提示词写进 `prompt.txt`，在 [控制台]({keys}) 创建 Key，然后运行：',
        ],
        'recreate_after': '用浏览器打开 `{html_out}`，或在 [SandBase Sandbox]({sandbox}) 中运行，让生成的代码保持隔离。上面的示例把 `max_tokens` 设为 128000，避免长页面被截断。完整步骤见 [教程](docs/zh-CN/tutorial.md)，价格见 [模型页]({model_page})。',
        'prompt_tag': '提示词',
        'more': '**[在 SandBase Lab 查看全部 {n} 条 →]({lab_section})**',
        'faq': '常见问题',
        'faq_items': [
            ('GPT-6.2 Astra 是什么？', 'GPT-6.2 Astra 是 OpenAI 的模型，2026 年 11 月 1 日宣布。本合集的创作者把它和 Claude Opus 5.5、Fable 5.5 放在一起运行。在 SandBase 上它的 ID 是 `{model_id}`。'),
            ('这些 GPT-6.2 Astra 视频是怎么做出来的？', '模型并不直接渲染视频。它写出一个网页，作者再把页面播放过程录下来。见 [教程](docs/zh-CN/tutorial.md)。'),
            ('在哪里找到视频的提示词？', '标有 **提示词** 的视频，其 Lab 页面上有作者的提示词。[提示词索引](docs/zh-CN/prompts.md) 列出了全部。'),
            ('怎么写好 GPT-6.2 Astra 提示词？', '指定输出一个独立的 HTML 文件，并说明用哪种渲染方式；描述场景，以及录屏需要捕捉的状态；禁止外部素材，并让模型自测页面。详细写法和模板见 [提示词写法](docs/zh-CN/prompt-guide.md)。'),
            ('怎么调用 GPT-6.2 Astra API？', '在 SandBase 上模型 ID 是 `{model_id}`，使用兼容 OpenAI 的 `/v1/chat/completions` 接口。见 [复刻](#recreate) 和 [模型页]({model_page})。'),
            ('GPT-6.2 Astra 比 Fable 5.5 或 Claude Opus 5.5 更强吗？', '目前的证据是创作者的单次运行，结论并不一致。同一个打斗火柴人提示词，GPT-6.2 Astra 花费 $1.65，Fable 5.5（Claude Code 中运行）为 $15.71，Opus 5.5（不使用工具）为 $1.11。在一张与 Fable 5.5 Max 并排展示的鹈鹕 SVG 上，作者称两者都"相当惊艳"，并请观众投票。本合集目前没有 GPT-6.2 Astra 的实测结果：它的 Evals 和 Pelican Test 数据未在本合集的数据来源中。详见 [模型对比](docs/zh-CN/model-comparison.md)。'),
            ('做一个视频要花多少钱？', '一位创作者报告，GPT-6.2 Astra 完成火柴人提示词的一次运行花费 $1.65；同一提示词下 Fable 5.5 为 $15.71，Opus 5.5 为 $1.11。这些都是作者自己设置下的单次运行。标价见 [模型页]({model_page})。'),
            ('可以转用这些视频吗？', '默认不可以，视频归作者所有。见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。'),
        ],
        'contribute': '推荐作品',
        'contribute_body': '发现了应该收录的 GPT-6.2 Astra 作品？附上 X 原帖 [提交给我们]({repo_url}/issues/new?template=submit-video.yml)。通过后会先加入 SandBase Lab，下一次每日同步时出现在这里。觉得有用的话，点个 ⭐ 能让更多人看到。',
        'credits': '致谢与权利',
        'credits_body': [
            '所有视频、提示词和帖子归作者所有。每张卡片都注明作者并链接原帖。MIT 许可证只覆盖本仓库的脚本。更正署名或下架视频请见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。',
            '{not_affiliated}',
        ],
        'footer': '由 [SandBase Lab]({lab_home}) 维护 · [全部 AI 视频合集]({all_collections})',
        'p_title': 'GPT-6.2 Astra 提示词',
        'p_switch': '[English](../prompts.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)',
        'p_intro': '共 {n} 条 GPT-6.2 Astra 视频，作者公开了提示词。打开即可查看提示词、观看视频，并在 SandBase Lab 上用 {short} 一键 **复刻**。第一次写 {short} 提示词？先看 [提示词写法](prompt-guide.md)。',
        'p_note': '每条都按 X 上发布的原文引用作者帖子。有的作者描述的是任务而不是完整提示词，请打开 X 原帖查看完整讨论串。帖子原文保留作者语言。',
        'p_watch': '观看',
        'p_open': '在 SandBase Lab 复刻',
    },
}

# Labels mirror shared/ai-videos.ts VIDEO_CATEGORIES in the Lab repo.
CATEGORIES = {
    '3d-scene': ('3D scenes', '3D 场景'),
    'motion-graphics': ('Motion graphics', '动效'),
    'game': ('Games', '游戏'),
    'ui-demo': ('Product UI', '产品界面'),
    'particles': ('Particles & shapes', '粒子与形状'),
    'data-viz': ('Charts & diagrams', '图表图解'),
    'kinetic-type': ('Kinetic type', '文字动效'),
    'explainer': ('Explainers', '讲解'),
    'launch-film': ('Launch films', '发布片'),
    'short-film': ('Short films', '短片'),
    'music-video': ('Music videos', '音乐视频'),
    'anime': ('Anime', '动画'),
    'action': ('Action', '动作'),
    'ad': ('Ads', '广告'),
    'comparison': ('Tests & comparisons', '测试对比'),
    'showcase': ('Model showcases', '模型展示'),
}


def utm(medium, content=None):
    q = f'utm_source=github&utm_medium={medium}&utm_campaign={CFG["campaign"]}'
    return q + (f'&utm_content={content}' if content else '')
