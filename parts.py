import streamlit as st

st.set_page_config(layout='wide')
if "page" not in st.session_state:
    st.session_state.page = "home"
tabs = st.tabs(["Home"])    
def go_fittings():
    st.session_state.page = "fittings"

def go_home():

    st.session_state.page = "home"

def go_contact():
    st.session_state.page = "contact"
hydraulic = "https://m.media-amazon.com/images/I/617QrwH+G+L.jpg"
hardware = "https://m.media-amazon.com/images/I/81Npb2nUV7L._UF1000,1000_QL80_.jpg"
image = "https://www.udtrucks.com/sites/default/files/styles/hero_desktop_crop/public/2024-01/Full_lineup_2024_Website%20Hero_0.jpg?itok=PgCxZ6EX"    
workshop_coupling_fittings = "https://jacosuperiorproducts.com/cdn/shop/products/Main.png?v=1611431622"    
coolant_coupling_fittings = "https://m.media-amazon.com/images/I/61Tad+YCNeL._UF894,1000_QL80_.jpg"
air_coupling_fittings = "https://m.media-amazon.com/images/I/81UaOlPopfL.jpg"
low_medium_pressure_fittings = "https://www.parker.com/content/dam/Parker-com/Online/Product-Images/Parflex-Division/zoom_1000x1000/TypeMAdapters_zm.jpg"
air_condition_fittings = "https://m.media-amazon.com/images/I/61L0eenASzL._UF894,1000_QL80_.jpg"
ligthing_url = "https://marathontruckparts.com/wp-content/uploads/2016/12/TL257M-400x400.jpg"
exhaust_system_url = "https://www.actiontrucks.com/cache/images_category-tiles_exhaust_tips_w400_h400_q80_t1698225443.jpg"
engine_parts_url = "https://scdn.autodoc.de/catalog/categories/600x600/200026.png"
batteries_url = "https://www.batteriessunshinecoast.com.au/wp-content/uploads/2025/06/N150-Truck-Battery.jpg"
suspension_url = "https://www.hendrickson-intl.com/getattachment/f4b7e4c8-6e3d-487d-b000-4bf76ceb2d49/RT_001-2-22-07_Trans.png"
oil_url = "https://i.ebayimg.com/00/s/NTAwWDUwMA==/z/D5sAAOSwQPlV-XbP/$_12.JPG"
fittings_URL = "https://pimimages.buyersproducts.com/products/MD/BUCOP375_profile.jpg"
oil_filter_url = "https://thumbs.dreamstime.com/b/oil-filters-20508237.jpg"


st.button("Home",on_click=go_home)

if st.session_state.page == "home":
    st.image("MY LOGO.jpg")
    st.image(image)
    

    columns = st.columns(4)
    with columns[0]:
        st.subheader("Suspension")
        st.image(suspension_url, caption="Suspension")
            
            
            
            

    with columns[1]:
        st.subheader("Truck Fittings")
        st.image(fittings_URL, caption="Fittings")
        st.button("View more", on_click = go_fittings)
            
            
            

    with columns[2]:
        st.subheader("Oil filter")
        st.image(oil_filter_url, caption="Oil filter")
        st.button("View more?")
            
            
            

    with columns[3]:
        st.subheader("Batteries")
        st.image(batteries_url, caption="Batteries")
            
            
            
            
            
            

        col2 = st.columns(4)
    with col2[0]:
        st.subheader("Engine parts")
        st.image(engine_parts_url, caption="Engine parts")
            
            
            
            
            
    with col2[1]:
        st.subheader("Truck Oil")
        st.image(oil_url, caption="Oil")
            
            
            
            
            
    with col2[2]:
        st.subheader("Exhaust System")
        st.image(exhaust_system_url, caption="Exhaust system")
            
            
            
            
    with col2[3]:
        st.subheader("Lightings")
        st.image(ligthing_url, caption="Lightings")
            
            
            
            

        submitted = st.button("Submit!")
        if submitted:
            go_contact()
          
elif st.session_state.page == "fittings":
    st.title("Fittings")
    columns = st.columns(5)
    
    
    with columns[0]:
        st.image(air_condition_fittings)
        st.write("Air Conditioning Fittings")
        st.subheader("$1/Piece")
        st.number_input("How much",max_value=100,min_value=1,step=1,key="fittings1")
        
    with columns[1]:
        st.image(low_medium_pressure_fittings,width=500 )
        st.write("Low Medium Pressure Fittings")
        st.subheader("$1/Piece")
        st.number_input("How much",max_value=100,min_value=1,step=1,key="fittings2")
         
    with columns[2]:
        st.image(air_coupling_fittings)
        st.write("Air Coupling Fittings")
        st.subheader("$1/Piece")
        st.number_input("How much",max_value=100,min_value=1,step=1,key="fittings3")   
         
    with columns[3]:
        st.image(coolant_coupling_fittings)  
        st.write("Coolant Coupling Fittings   $1/Piece")
        st.subheader("$1/Piece")
        st.number_input("How much",max_value=100,min_value=1,step=1,key="fittings4")
        
    col2 = st.columns(3)
    with col2[0]:
        st.image(workshop_coupling_fittings,width=150)
        st.write("Workshop  Coupling  Fittings")
        st.subheader("$1/Piece")
        st.number_input("How much",max_value=100,min_value=1,step=1,key="fittings5")
    with col2[1]:
        st.image(hardware,width=220)
        st.write("Hardware Fittings")
        st.subheader("$1/Piece")
        st.number_input("How much",max_value=100,min_value=1,step=1,key="fittings6")
    with col2[2]:
        st.image(hydraulic,width=150)
        st.write("Hydraulic Coupling Fittings")
        st.subheader("$1/Piece")
        st.number_input("How much",max_value=100,min_value=1,step=1,key="fittings7")
        
        

        



elif st.session_state.page == "contact":
    st.title("Customer Details")
    with st.form("info_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        pf = st.text_input("Phone Number (optional)")
        ac = st.text_area("Additional Comments (optional)")

        submitted = st.form_submit_button("Submit Info")
        

        if submitted:
            if name == "":
                st.warning("Please enter your name")
            elif email == "":
                st.warning("Please enter your email")
            
            else:
                    
                st.success("Info submitted successfully!")
                    

































