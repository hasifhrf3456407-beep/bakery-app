
import streamlit as st

st.set_page_config(
    page_title="এ - HR Business App",
    page_icon="🅰️",
    layout="wide"
)

# App Title
st.title("🅰️ এ - HR Business App")

# Sidebar Menu
st.sidebar.header("কন্ট্রোল প্যানেল")
menu = st.sidebar.selectbox(
    "মেনু নির্বাচন করুন",
    ["ড্যাশবোর্ড", "🤖 AI সহকারী", "ক্রয়কৃত মাল", "বিক্রিত মাল", "রেসিপি ম্যানেজমেন্ট"]
)

if menu == "ড্যাশবোর্ড":
    st.header("📊 সার্বিক অবস্থা")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("মোট কাঁচামাল আইটেম", "৯টি")
    with col2:
        st.metric("আজকের প্রোডাকশন", "৬০ কার্টুন")

elif menu == "🤖 AI সহকারী":
    st.header("🤖 AI সহকারী (Assistive Intelligence)")
    st.write("আপনার ফ্যাক্টরি ও ব্যবসার যেকোনো প্রশ্নের উত্তর বা পরামর্শের জন্য নিচে লিখুন:")
    
    user_query = st.text_input("আপনার প্রশ্ন বা নির্দেশ লিখুন:")
    if st.button("AI-কে জিজ্ঞাসা করুন"):
        if user_query:
            st.success(f"AI উত্তর দিচ্ছে: '{user_query}' সংক্রান্ত তথ্য প্রক্রিয়াধীন...")
            st.info("আপনার ইনভেন্টরি ও রেসিপির ডেটা অনুযায়ী AI সহকারী সাজেস্ট করছে।")
        else:
            st.warning("দয়া করে একটি প্রশ্ন লিখুন।")

elif menu == "ক্রয়কৃত মাল":
    st.header("📦 ক্রয়কৃত কাঁচামালের তালিকা")
    st.write("১. ময়দা")
    st.write("২. চিনি")
    st.write("৩. প্যাকেজিং পার্টি")
    st.write("৪. পেস্ট্রি মার্জারিন (৫০০/- টাকা)")
    st.write("৫. স্পেশাল ভ্যানিলা স্পঞ্জ পাউডার (৩২০/- টাকা/কেজি)")
    st.write("৬. জি এম এস পাউডার")
    st.write("৭. পুষ্টি মার্জারিন (১ কার্টুন = ১৫ কেজি)")
    st.write("৮. সল্ট ডালডা (১ কার্টুন = ১৬ কেজি)")

elif menu == "বিক্রিত মাল":
    st.header("🚚 বিক্রিত মালের রেকর্ড (স্টার লাইন ফুডস)")
    st.write("• পুষ্টি মার্জারিন")
    st.write("• বাটার ক্রিম: ৬০ কার্টুন")

elif menu == "রেসিপি ম্যানেজমেন্ট":
    st.header("📜 স্পঞ্জ পাউডার ভ্যানিলা রেসিপি (১০০ কেজি / ৫ কার্টুন)")
    st.write("১. ময়দা: ৪৮ কেজি")
    st.write("২. চিনি: ৪০ কেজি")
    st.write("৩. অন্যান্য উপকরণ: ১২ কেজি")
