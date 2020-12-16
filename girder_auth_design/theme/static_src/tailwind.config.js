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
    fontSize: {
      'tiny': '.65rem',
      'xs': '.75rem',
      'sm': '.875rem',
      'base': '1rem',
      'lg': '1.125rem',
      'xl': '1.25rem',
      '2xl': '1.5rem',
      '3xl': '1.875rem',
      '4xl': '2.25rem',
      '5xl': '3rem',
      '6xl': '4rem',
    },
    maxWidth: {
      '1/4': '25%',
      '1/2': '50%',
      '3/4': '75%',
    },
    extend: {
      boxShadow: {
        outline: '0 0 0 3px #BFDBFE',
        'inner-large': 'inset 0 -6px 20px 0 rgba(0, 0, 0, 0.06)',
      },
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
