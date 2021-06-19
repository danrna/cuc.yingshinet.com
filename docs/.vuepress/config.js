module.exports = {
  base: process.env.VUEPRESS_BASE || "/",
  title: "数据可视化原理与实例",
  description: "数据之美",
  head: [
    ["link", { rel: "icon", href: `/logo.png` }],
    ["meta", { name: "theme-color", content: "#0078E7" }],
    ["meta", { name: "apple-mobile-web-app-capable", content: "yes" }],
    [
      "meta",
      { name: "apple-mobile-web-app-status-bar-style", content: "black" },
    ],
    ["meta", { name: "msapplication-TileColor", content: "#000000" }],
    // ['meta', { 'http-equiv': 'Content-Security-Policy', content: 'upgrade-insecure-requests' }]
  ],
  themeConfig: {
    logo: "/logo.png",
    smoothScroll: true,
    repo: "cbd-lab/cuc.yingshinet.com",
    editLinks: true,
    editLinkText: "帮助我们改善此页面！",
    nav: [
      {
        text: "原理",
        link: "/guide/",
      },
      {
        text: "实例",
        link: "/demo/",
      },
      {
        text: "中国大学MOOC",
        link: "https://www.icourse163.org/course/CUC-1206407806",
      },
    ],
    sidebar: [
      {
        title: "《数据可视化原理与实例》",
        path: "https://item.jd.com/12467892.html",
      },
      {
        title: "原理", // 必要的
        collapsable: false,
        sidebarDepth: 3,
        children: [
          ["/ch1/", "第一章 基于 Web 的数据可视化基础"],
          ["/ch2/", "第二章 基于 JavaScript 和 SVG 的绘图"],
          ["/ch3/", "第三章 D3 数据可视化基础"],
          ["/ch4/", "第四章 D3 饼图环图和玫瑰图"],
          ["/ch5/", "第五章 D3 比例尺与配色"],
          ["/ch6/", "第六章 D3 动画与交互"],
          ["/ch7/", "第七章 D3 力导向布局"],
          ["/ch8/", "第八章 地图可视化"],
          ["/ch9/", "第九章 音乐可视化"],
          ["/ch10/", "第十章 Canvas 与图像处理"],
          ["/ch11/", "第十一章 数据可视化之数据获取"],
          ["/ch12/", "第十二章 分词与词云图可视化"],
          ["/ch13/", "第十三章 一种基于占用矩阵的词云图可视化算法"],
        ],
      },
      {
        title: "实例",
        collapsable: false,
        children: [
          ["/show/", "作品展示"],
          {
            title: "视频课程",
            path: "/course/",
            children: [
              ["/course/CH1.html", "CH1"],
              ["/course/CH2.html", "CH2"],
              ["/course/CH3.html", "CH3"],
              ["/course/CH4.html", "CH4"],
              ["/course/CH7.html", "CH7"],
              ["/course/CH8.html", "CH8"],
              ["/course/CH10.html", "CH10"],
              ["/course/Flask.html", "Flask"],
            ],
          },
          ["/demo/", "Demo 下载"],
        ],
      },
    ],
  },
  plugins: ["@vuepress/back-to-top"],
};
