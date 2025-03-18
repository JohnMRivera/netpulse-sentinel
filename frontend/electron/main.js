import { app, BrowserWindow } from 'electron'

let window

app.whenReady().then(() => {
    window = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences:{
            nodeIntegration: true
        }
    })

    window.loadURL(`http://${process.env.FRONTEND_HOST}:${process.env.FRONTEND_PORT}`)
})