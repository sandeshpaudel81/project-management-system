/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        screens: {
            sm: '640px',
            md: '768px',
            lg_3: '732px',
            lg_2: '832px',
            lg_1: '932px',
            lg: '1024px',
            xl_1: '1132px',
            xl: '1280px',
            '2xl': '1530px',
        },
        extend: {},
        colors: {
            transparent: 'transparent',
            current: 'currentColor',
            'white': '#ffffff',
            'purple': '#3f3cbb',
            'midnight': '#121063',
            'metal': '#565584',
            'tahiti': '#3ab7bf',
            'silver': '#ecebff',
            'bubble-gum': '#ff77e9',
            'bermuda': '#78dcca',
            'black': '#000000',
            'gray': {
                200: '#e5e7eb',
                400: '#9ca3af',
                600: '#4b5563'
            },
            'slate': {
                300: '#cbd5e1',
                400: '#94a3b8',
                500: '#64748b',
            },
            'ultravoilet': '#5F4B8BFF',
            'bloomingdahila': '#E69A8DFF',
        },
        fontFamily: {
            poppins: ['Poppins', 'sans-serif'],
            notosans: ['Noto Sans', 'sans-serif'],
        },
        minHeight: {
            '1/2': '50vh',
            '4/5': '80vh',
            'screen': '100vh'
        },
        maxHeight: {
            '4/5': '80vh',
            'screen': '100vh'
        }
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),

        require('tailwind-scrollbar'),
        require('tailwind-scrollbar-hide'),
    ],
}
