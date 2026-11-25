# pairwise-multiband-compressor-crossover

## 领域

游戏、图形与多媒体

## 主题

多段压缩器分频相位

## 说明

Linkwitz-Riley 分频、跨段包络联动、系数双缓冲。

初始状态下 `av/multiband_comp.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
