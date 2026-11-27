import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'zh-CN',
  title: '固体物理',
  description: '固体物理课程要点与分级习题集',
  base: '/solid-state-physics/',

  markdown: {
    math: true
  },

  themeConfig: {
    nav: [],

    sidebar: [
      {
        text: '课程说明',
        items: [
          { text: '课程简介', link: '/' }
        ]
      },
      {
        text: '结构、结合与晶格动力学',
        items: [
          { text: '01-晶体结构', link: '/ch01-crystal-structure' },
          { text: '02-晶体的结合', link: '/ch02-crystal-bonding' },
          { text: '03-晶格振动与晶体的热学性质', link: '/ch03-lattice-vibrations' }
        ]
      },
      {
        text: '金属、能带与半导体',
        items: [
          { text: '04-金属电子理论', link: '/ch04-free-electron' },
          { text: '05-固体的能带理论', link: '/ch05-band-theory' },
          { text: '06-半导体电子理论', link: '/ch06-semiconductors' }
        ]
      },
      {
        text: '综合练习',
        items: [
          { text: '综合-跨章节典型题', link: '/synthesis' }
        ]
      }
    ],

    outline: {
      level: [2, 3],
      label: '本页目录'
    },

    docFooter: {
      prev: '上一章',
      next: '下一章'
    },

    darkModeSwitchLabel: '外观',
    sidebarMenuLabel: '目录',
    returnToTopLabel: '返回顶部',

    socialLinks: [
      { icon: 'github', link: 'https://github.com/yijun-yu/solid-state-physics' }
    ]
  }
})
