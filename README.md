# 餐廳訂位系統 - 演算法期中專案

## 簡介
本專案是一個使用 **Flask** 為後端框架、**HTML/CSS/JavaScript** 為前端技術的 **餐廳訂位系統**。  
系統提供以下基本功能：
- 新增訂位
- 查詢訂位（依顧客姓名或電話號碼）
- 列出所有訂位

此專案旨在展示簡單演算法於資料管理和檢索中的應用。

---

## 介面預覽

以下是系統介面的預覽畫面：

![image](https://github.com/user-attachments/assets/b7b544cd-6c3f-479f-965a-508cb41995ed)

---

## 功能特色
### 1. 新增訂位  
用戶可輸入顧客姓名與電話號碼，將資料儲存於系統中。

### 2. 查詢訂位  
- **依姓名查詢**：用戶可根據顧客姓名查詢訂位。  
- **依電話號碼查詢**：用戶可根據顧客電話號碼查詢訂位。

### 3. 列出所有訂位  
顯示目前儲存在系統中的所有訂位資料。

---

## 系統架構

### 後端
- **框架**：Flask
- **API 端點**：
  - `/add_reservation`：新增訂位。
  - `/search_reservation`：根據姓名查詢訂位。
  - `/search_by_phone`：根據電話號碼查詢訂位。
  - `/list_reservations`：列出所有訂位資料。

### 前端
- **HTML**：構建頁面結構。
- **CSS**：設計樣式，包含自訂樣式與 **Bootstrap** 響應式設計。
- **JavaScript**：使用 **Fetch API** 與後端進行互動。

### 演算法
- **線性搜尋**：用於根據姓名或電話號碼檢索訂位資料。
- **資料管理**：採用基本的 Python 資料結構（如列表或字典）儲存訂位。

---

## 使用說明

### 1. 環境設置
安裝必要的套件：
```bash
pip install -r requirements.txt
```
（目前僅需安裝 Flask）

### 2. Start the Server
使用以下指令啟動伺服器：

```bash
python app.py
```

或使用 Flask 提供的開發伺服器：
```bash
flask run
```

伺服器將運行於：
```arduino
http://127.0.0.1:5000
```
### 3. 開啟前端
在瀏覽器中打開`index.html`，即可使用系統。

---

## 專案結構

- **app.py**：使用 Flask 建立的後端應用程式，處理 API 請求。
- **reservation_system.py**：包含訂位邏輯的核心 Python 程式。
- **requirements.txt**：列出專案所需的 Python 套件。
- **.gitignore**：指定 Git 需忽略的檔案與目錄。

### 資料夾：
- **static**：包含前端靜態資源。
  - **script.js**：用於處理用戶操作與 API 請求的 JavaScript 檔案。
  - **style.css**：前端自訂樣式檔案。
- **templates**：存放前端 HTML 模板。
  - **index.html**：系統的主要用戶界面。

---



## Contributor

- **姓名**: 蔣哿樂 (CHIANG, KE-LE)  
- **學號**: 111113201  
- **專案名稱**: 餐廳訂位系統 (Restaurant Reservation System)





