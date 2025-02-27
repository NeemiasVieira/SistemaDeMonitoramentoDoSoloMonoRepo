import { createGlobalStyle } from 'styled-components';

export const LightTheme = createGlobalStyle`
    body {
        margin: 0;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
            'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
            sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        background-color: var(--bg-primary);
    }

    html::-webkit-scrollbar {
        width: 10px;
    }

    html::-webkit-scrollbar-track {
        background: #222;
    }

    html::-webkit-scrollbar-thumb {
        background-color: var(--dark-green);
        border: solid #53AF30 1.5px;
        border-radius: 5px;
    }

    code {
        font-family: 'Montserrat', sans-serif, source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
            monospace;
    }

    :root {
        --gray-primary: #6B6B6B;
        --bg-dark-blue: #054472;
        --contrast: #fff;
        --light-green: #8CDF27;
        --dark-green: #53BF30;
        --force-dark-green: #53BF30;
        --bg-primary: #E1E1E1;
        --text-secondary: #444;
        --text-primary: #000;
        --border-primary: #ccc;
        --border-secondary: #222;
        --border-constrast: #000;
        --button-primary: #fff;
        --footer: #222;
        --border-hover: #222;
        --bg-modal: rgba(0, 0, 0, 0.5);
        --red: #ff2200;
        --light-gray: #ddd;
        --super-light-gray: #f5f5f5;
        --white: #fff;
        --disabled-button-bg: #ccc;
        --disabled-button-color: #fff;
    }
`;
