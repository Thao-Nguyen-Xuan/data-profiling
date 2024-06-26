import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report  

st.title("HÃY ĐỂ TÔI PHÂN TÍCH DỮ LIỆU CỦA BẠN")

file = st.file_uploader("Tải file dữ liệu (xlsx, csv) ở đây",type=["xlsx", "csv"], accept_multiple_files=False)
if file:       
    file_extension = file.name.split(".")[-1]
    if file_extension == "xlsx":
        df = pd.read_excel(file,index_col = None)
    elif file_extension == "csv":
        df = pd.read_csv(file,index_col = None)
    else:
        st.error("Định dạng không được hỗ trợ. Vui lòng chọn file Excel hoặc CSV.")
        st.stop()
    st.dataframe(df)

if st.button("Tạo báo cáo"):
    if df is not None:
        profile_report = ProfileReport(df)
        st_profile_report(profile_report)
        with open('profile_report.html', 'w', encoding='utf-8') as f:
            f.write(profile_report.to_html())
        st.download_button('Download Báo cáo', data=profile_report.to_html(), file_name='Profile Report.html', mime='text/html')
    else:
        st.warning("Vui lòng tải tập dữ liệu của bạn lên trước ⚠️")
            


