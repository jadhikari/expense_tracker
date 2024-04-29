# Install tailwindcss process

Initialize npm in your project
npm init -y


Install Tailwind CSS:
npm install tailwindcss postcss autoprefixer


Create a Tailwind CSS configuration file: Generate a tailwind.config.js file in your project's root directory:
npx tailwindcss init


Create Your CSS File:

/* ./myproject/static/css/styles.css */
@tailwind base;
@tailwind components;
@tailwind utilities;


Build Your CSS File: Add a script to your package.json to build your CSS file. Open package.json and add a "build" script under "scripts":

"scripts": {
    "build": "postcss static/css/styles.css -o static/css/output.css"
}


Run the Build Script:
npm run build
