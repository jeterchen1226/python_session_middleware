透過 SessionMiddleware 管理使用者狀態，經由`secrets`產生 secret_key，所以不需要自行創建。
### 測試
`/hello`用來產生 session 簽章，讓前後端能夠自由溝通，當點擊`/talk`時會透過 secret_key 所產生的簽章做回應知道現在要做什麼事。