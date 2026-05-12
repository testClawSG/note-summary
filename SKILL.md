---
name: note-summary
description: 获取用户的备忘录内容，通过调用脚本进行内容总结。
tools:
 -search_notes
---

# summarize_text

## 触发条件
当用户提到以下内容时，使用该技能: "进行备忘录总结","总结备忘录"等
## 使用方法
首先使用search_notes获取用户要求的备忘录内容
调用note-summary.py,将备忘录内容合并一行，作为命令行参数，发送出去


