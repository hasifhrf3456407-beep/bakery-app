import streamlit as st

st.set_page_config(page_title="Factory Management App", layout="wide")

st.title("🏭 ফ্যাক্টরি ইনভেন্টরি ও প্রোডাকশন অ্যাপ")

menu = st.sidebar.selectbox("মেনু নির্বাচন করুন", ["ড্যাশবোর্ড", "কাঁচামাল স্টক", "প্রোডাকশন ও রেসিপি", "বিক্রি ও পার্টি"])

if menu == "ড্যাশবোর্ড":
    st.header("📊 সার্বিক অবস্থা")
    st.metric(label="মোট কাঁচামাল আইটেম", value="৯টি")
    st.metric(label="আজকের প্রোডাকশন", value="৬০ কার্টুন")

elif menu == "কাঁচামাল স্টক":
    st.header("📦 কাঁচামাল ইনভেন্টরি")
    st.write("১. ময়দা (Flour)")
    st.write("২. চিনি (Sugar)")
    st.write("৩. পুষ্টি মার্জারিন (Pusti Margarine - 15kg/cartoon)")
    st.write("৪. সল্ট ডালডা (Salt Dalda - 16kg/cartoon)")

elif menu == "প্রোডাকশন ও রেসিপি":
    st.header("🥣 স্পঞ্জ পাউডার ভ্যানিলা রেসিপি (১০০ kg)")
    st.write("- ময়দা: ৪৮ kg")
    st.write("- চিনি: ৪০ kg")
    st.write("- অন্যান্য: ১২ kg")

elif menu == "বিক্রি ও পার্টি":
    st.header("🚚 বিক্রিত মাল ও পার্টি")
    st.write("স্টোরকিপার ও এডমিন এন্ট্রি অপশন এখানে যুক্ত হবে।")
