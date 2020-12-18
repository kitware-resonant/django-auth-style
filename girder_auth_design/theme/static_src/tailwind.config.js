// This is a minimal config.
// If you need the full config, get it from here:
// https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
const colors = require('tailwindcss/colors')

module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    fontFamily: {
      'sans': 'Nunito, sans-serif'
    },
    extend: {
      colors: {
        'keppel': {
          '50': '#f6fcfb',
          '100': '#edf9f7',
          '200': '#d1efeb',
          '300': '#b5e5df',
          '400': '#7ed2c8',
          '500': '#46beb0',
          '600': '#3fab9e',
          '700': '#358f84',
          '800': '#2a726a',
          '900': '#225d56'
        },
        'supernova': {
          '50': '#fffdf4',
          '100': '#fffae9',
          '200': '#fff3c8',
          '300': '#ffeca7',
          '400': '#ffdd66',
          '500': '#ffcf24',
          '600': '#e6ba20',
          '700': '#bf9b1b',
          '800': '#997c16',
          '900': '#7d6512'
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
      width: {
        '120': '30rem',
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
