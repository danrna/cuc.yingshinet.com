module.exports = {
  title: '数据可视化原理与实例',
  description: '数据之美',
  head: [
    ['link', { rel: 'icon', href: `/logo.png` }],
    ['meta', { name: 'theme-color', content: '#0078E7' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black' }],
    ['meta', { name: 'msapplication-TileColor', content: '#000000' }]
  ],
  themeConfig: {
    smoothScroll: true,
    sidebar: [
      {
        title: '原理',   // 必要的
        children: [
          {
            title: '第一章 基于 Web 的数据可视化基础',
            path: '/ch1/',
            children: [
              ['/ch1/sect1.html', '第一节 数据可视化概述'],
              ['/ch1/sect2.html', '第二节 HTML文档']
            ]
          },
          {
            title: '第二章 基于 JavaScript 和 SVG 的绘图',
            path: '/ch2/', 
            children: [
              '/ch2/histogram',
              '/ch2/bintree',
              '/ch2/tree-word-cloud'
            ]
          },
          ['/ch1/', '第三章 D3 数据可视化基础'],
          ['/ch1/', '第四章 D3 饼图环图和玫瑰图'],
          ['/ch1/', '第五章 D3 比例尺与配色'],
          ['/ch1/', '第六章 D3 动画与交互'],
          ['/ch1/', '第七章 D3 力导向布局'],
          ['/ch1/', '第八章 地图可视化'],
          ['/ch1/', '第九章 音乐可视化'],
          ['/ch1/', '第十章 Canvas 与图像处理'],
          ['/ch1/', '第十一章 数据可视化之数据获取'],
          ['/ch1/', '第十二章 分词与词云图可视化'],
          ['/ch1/', '第十三章 一种基于占用矩阵的词云图可视化算法']
        ]
      },
      {
        title: '实例',
        children: [
          ['/ch1/', '作品展示'],
          ['/ch1/', '视频课程'],
          ['/ch1/', 'Demo 下载']
        ]
      }
    ]
  }
}