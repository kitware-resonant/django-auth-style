// This is a minimal config.
// If you need the full config, get it from here:
// https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
const colors = require('tailwindcss/colors')

module.exports = {
  purge: false,
  darkMode: false, // or 'media' or 'class'
  theme: {
    fontFamily: {
      'sans': 'Nunito, sans-serif'
    },
    extend: {
      colors: {
        'accent': {
          '50': '#fafdf8',
          '100': '#f6fbf1',
          '200': '#e8f4db',
          '300': '#d9eec5',
          '400': '#bde19a',
          '500': '#a1d46e',
          '600': '#91bf63',
          '700': '#799f53',
          '800': '#617f42',
          '900': '#4f6836'
        },
        'secondary': {
          '50': '#f2fafd',
          '100': '#e6f5fb',
          '200': '#bfe5f5',
          '300': '#99d5ef',
          '400': '#4db6e4',
          '500': '#0097D8',
          '600': '#0088c2',
          '700': '#0071a2',
          '800': '#005b82',
          '900': '#004a6a'
        },
        'primary': {
          '50': '#f3f8fb',
          '100': '#e8f0f8',
          '200': '#c5dbed',
          '300': '#a2c5e2',
          '400': '#5c99cc',
          '500': '#166DB6',
          '600': '#1462a4',
          '700': '#115289',
          '800': '#0d416d',
          '900': '#0b3559'
        }
      },
      fontSize: {
        '2xs': '.7rem',
        '3xs': '.63rem',
      },
      maxWidth: {
        '2xs': '16rem',
        '3xs': '12rem',
      },
      minWidth: {
        '2xs': '16rem',
        '3xs': '12rem',
      },
    },
  },
  variants: {
    extend: {
      borderWidth: ['last'],
      display: ['hover', 'focus', 'group-hover', 'group-focus'],
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
