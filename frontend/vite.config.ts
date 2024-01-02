import { defineConfig } from 'vite'
import wyw from '@wyw-in-js/vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react(), wyw()],
})
