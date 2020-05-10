from selenium import webdriver
brwsr = webdriver.Chrome()
brwsr.get("https://st.prntscr.com/2020/05/08/0312/img/0_173a7b_211be8ff.png")
brwsr.save_screenshot("sc.png")