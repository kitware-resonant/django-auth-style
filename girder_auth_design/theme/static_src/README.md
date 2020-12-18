# Configuring Tailwind

## The config file

For convenience, certain configurations have been added to `tailwind.config.js`. Among these changes are:

1. Tailwind's default `sans` property changed to custom Google Font, Nunito. The font is linked in the `<head>` of `core/templates/account/base.html` and then defined in the Tailwind config.
2. Extended color palette, adding `primary`, `secondary` and `accent` color families.
   - **For example:** To set a background color you would use `bg-{color}-{50-900}`. For this example I'll use `bg-blue-500`. With the extended color palette, you will now be able to use `bg-primary-500`, `bg-secondary-500` or `bg-accent-500`.
   - You may want to define your own colors, or replace the theme colors defined in the config. For your convenience, you may use [this tool](https://javisperez.github.io/tailwindcolorshades/) to generate all of the shades.
3. Smaller font sizes for when space is an issue. You may use `text-2xs` or `text-3xs` classes to set the font a little smaller than tailwind's smallest size of `text-xs`.
4. Smaller `min-width` and `max-width` values. Similarly to font sizes, you can now use `max-w-2xs`, `max-w-3xs`, `min-w-2xs` and `min-w-3xs`.

## The stylesheet

When using base Tailwind, all styles are reset and things like links, headings, form elements, etc. are completely unstyled. To alleviate this, some global default styles for some of these things have been added.

1. `html` and `body` styles have been provided.
2. Global styles for links have been added.
3. Global heading styles added, defining a hierarchy using font sizes, font weights and color.
4. Button styles have been added (see next section).
5. Global styles for form fields have been added.

### Button Styles

#### Button color classes
For when you want to use the different theme colors on your buttons. Best used for main action buttons.
- `.is-primary` - Creates a button that is set to the primary color.
- `.is-secondary` - Creates a button that is set to the secondary color.
- `.is-accent` - Creates a button that is set to the accent color.

#### Outlined class
For when you want the button to have slightly less impact. Best used for secondary action buttons.
- `.is-outline` - Creates an outlined button. (ie. using `class="button is-primary is-outline"` will create an outline button that is set to the primary color)

#### Button size classes
For when space is an issue (especially on smaller screen sizes).
- `.is-sm` - Creates a small button
- `.is-xs` - Creates an extra small button
