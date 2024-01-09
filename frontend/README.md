# **Start Frontend**
___
# Prerequisites
1. Node.js: Make sure you have [Node.js](https://nodejs.org/en) (18 or higher) installed on your machine.

# Steps
Open your terminal in the `frontend` folder, run the following command:
```bash
npm install # or npm i
```

check if all `.env.development` variables were set:
 - VITE_API_URL

then, run the command:
```bash
npm run dev
```

This starts running the project on [port 5173](http://localhost:5173/).

# **About**
___
# Technologies
- [TypeScript](https://www.typescriptlang.org)
- [Vite](https://vitejs.dev)
- [React](https://react.dev)
- [Linaria](https://linaria.dev)
- [Typescript-eslint](https://typescript-eslint.io)

# **Structure**
___

All changed files in the project must be located in the src folder. 
These files are organized in folders and have the following functions:

`assets:` Contains static assets such as images, fonts or other files used in the application.

`components:` Contains reusable and modular UI components. This can include buttons, forms, cards, and other smaller pieces that can be combined to build larger parts of your user interface.

`constants:` Stores constants or configuration settings used throughout the application. This can be configuration options or other static values.

`containers:`Contains components that act as containers for managing state and logic, orchestrating the flow of data and passing it to presentation components.

`enums:` Contains TypeScript enum declarations or similar structures as necessary.

`hooks:` Contains custom React hooks.

`layout:` Contains components and styles related to the overall layout of your app, such as header, footer, or sidebar components.

`lib:` Contains utility functions, helper classes, or third-party libraries.

`pages:` Contains components that represent different pages.

`services:` Contains code related to data fetching, API calls, or other services that interact with external resources.

`types:` Contains TypeScript type definitions. They can include custom types, interfaces, or type aliases.

# Components
## React Component
Each React component must be made up of a folder with the name `PascalCase`, with an `index.tsx` and a `styles.ts`
```shell
$ tree
.
└── src
    └── components
        └── CardExemple
            ├── index.tsx
            └── styles.ts
```

## Service Components
Each service component must be in a file with the indicative name of its function in `camelCase` with explicit exports of its function.

## Assets
Each Asset must have an indicative name in `kebab-case`.