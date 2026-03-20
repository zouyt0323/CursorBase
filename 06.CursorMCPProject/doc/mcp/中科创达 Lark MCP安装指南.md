**最近，飞书官方发布了飞书的MCP服务，今天在创达的飞书上构建了这个服务，欢迎大家配置使用。主要的使用场景：**

* **让编码工具Copilot、Cursor等，根据飞书的文档要求进行编码及其他相关总结工作等**
* **根据代码等编码工具内的信息，按用户要求更新文档或者整理新文档**
* **根据用户要求对飞书文档、表格进行整理、计算，生成报告等**
* **其他应用场景，等待大家挖掘。。。**

**具体配置步骤如下：**

1. 本地电脑安装[Node.js官网](https://nodejs.org/)（如果是Cursor或者类似IDE，可以直接用agent模式，让AI自己装）
2. 验证安装成功：

   ```Plain
   node -v
   npm -v
   ```
3. 打开IDE的终端，或者打开命令行执行终端，执行：

   ```Plain
   npx -y @larksuiteoapi/lark-mcp login -a cli_a8fde940c6da9013 -s tcxHbJIjVPUYrS61L92hKePrsQRYHolA
   ```
4. 一分钟内点击命令执行结果中的链接，在浏览器中进行飞书授权操作

5. 在你的IDE里面追加MCP的配置（以Cursor为例）：

追加以下内容到配置的json文件里：

```JSON
"lark-mcp": {
          "command": "npx",
          "args": [
            "-y",
            "@larksuiteoapi/lark-mcp",
            "mcp",
            "-a",
            "cli_a8fde940c6da9013",
            "-s",
            "tcxHbJIjVPUYrS61L92hKePrsQRYHolA",
            "--oauth"
          ]
        }
}
```

6. IDE的绿灯亮了，说明配置成功了。

**使用场景示意：**

1. **场景：** 让他帮我总结最近AI培训相关的会议资料、会议纪要等，并整理成Action Item List，发送给我。
2. **IDE对话内容（Agent模式）：** 帮我整理飞书上最近的视频会议记录及文档中关于AI培训的相关信息，整理成Action Item的清单，并生成一个新的文档，直接发送给贺涛（hetao@thundersoft.com）

3. **执行结果（IDE）：**

4. 执行结果（飞书消息&生成的飞书文档）：

**欢迎大家来尝鲜！！**