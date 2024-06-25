import type { Config } from 'tailwindcss';
import daisyui from 'daisyui';

export default {
  content: [
    './auth_style/templates/**/*.html',
  ],
  safelist: [
    // Injected by Django, and may be referenced by CSS rules
    'errorlist',
  ],
  theme: {
    fontFamily: {
      'sans': 'Nunito, sans-serif',
    },
  },
  plugins: [
    daisyui,
  ],
  daisyui: {
    logs: false,
    themes: [
      {
        'dgs': {
          'primary': '#0068c7',
          'primary-focus': '#00559e',
          'primary-content': '#ffffff',
          'secondary': '#3eae2b',
          'secondary-focus': '#2f8b23',
          'secondary-content': '#ffffff',
          'accent': '#499ce9',
          'accent-focus': '#499ce9',
          'accent-content': '#ffffff',
          'neutral': '#3d4451',
          'neutral-focus': '#2a2e37',
          'neutral-content': '#ffffff',
          'base-100': '#f6f8fa',
          'base-200': '#e7ebf2',
          'base-300': '#dce3ec',
          'base-content': '#3d4451',
          'info': '#4d95d8',
          'success': '#76AD6C',
          'warning': '#E4C062',
          'error': '#f42836',
        },
      },
    ],
  },
} satisfies Config;
