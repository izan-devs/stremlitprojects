import streamlit as st

st.set_page_config(layout='wide')
if "page" not in st.session_state:
    st.session_state.page = "home"
tabs = st.tabs(["Home"]) 
def go_filter():
    st.session_state.page = "filter"
def go_fittings():
    st.session_state.page = "fittings"

def go_home():

    st.session_state.page = "home"

def go_contact():
    st.session_state.page = "contact"
power = "https://m.media-amazon.com/images/I/71Cn2FAdxcL._UF350,350_QL50_.jpg"
transmission = "https://www.duallane.com/media/catalog/product/cache/a95e9d2b539204ab79c900aa251ba8eb/f/l/fleetguard-transmission-filter-hf28943.1.jpg"
water = "https://m.media-amazon.com/images/I/51NWojSF3tL.jpg"
feul = "https://cdn11.bigcommerce.com/s-26lddf/images/stencil/1280x1280/products/4673/19637/P551337__81487.1735036382.jpg?c=2"
air = "https://5.imimg.com/data5/AN/PC/MY-2352124/truck-air-filter-500x500.jpg"
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
        bcol = st.columns([1,3,1])
        with bcol[1]:
            st.button("View more?",key="one")
            
            
            
            

    with columns[1]:
        st.subheader("Truck Fittings")
        st.image(fittings_URL, caption="Fittings")
        with bcol[1]:
            st.button("View more", on_click = go_fittings)
            
            
            

    with columns[2]:
        st.subheader("Oil filter")
        st.image(oil_filter_url, caption="Oil filter")
        st.button("View more?",key="two",on_click = go_filter)
            
            
            

    with columns[3]:
        st.subheader("Batteries")
        st.image(batteries_url, caption="Batteries")
        st.button("View more?",key="three")
            
            
            
            
            
            

    
    with columns[0]:
        st.subheader("Engine parts")
        st.image(engine_parts_url, caption="Engine parts")
        st.button("View more?",key="four")
        submitted = st.button("Submit!")
        if submitted:
            go_contact()
            
            
            
            
            
    with columns[1]:
        st.subheader("Truck Oil")
        st.image(oil_url, caption="Oil")
        st.button("View more?",key="five")
            
            
            
            
            
    with columns[2]:
        st.subheader("Exhaust System")
        st.image(exhaust_system_url, caption="Exhaust system")
        st.button("View more?")
            
            
            
            
    with columns[3]:
        st.subheader("Lightings")
        st.image(ligthing_url, caption="Lightings")
        st.button("View more?",key="seven")
            
            
            
            

        
elif st.session_state.page == "filter":
    st.title("FILTERS")
    col3 = st.columns(5)
    with col3 [0]:
        st.image(air)
        st.write("Air Filter")
        st.subheader("$5")
        st.number_input("How much?",min_value=0,max_value=100,step=1,key="filter1")
    with col3[1]:
        st.image(feul)
        st.write("Feul Filter")
        st.subheader("$5")
        st.number_input("How much",min_value=0,max_value=100,step=1,key="filter2")
    with col3[2]:
        st.image(water)
        st.write("Water Filters")
        st.subheader("$5")
        st.number_input("How much",min_value=0,max_value=100,step=1,key="filter3")
    with col3[3]:
        st.image(transmission)
        st.write("Transmission Filter")
        st.subheader("$5")
        st.number_input("How much",min_value=0,max_value=100,step=1,key="filter4")
    with col3[4]:
        st.image(power)
        st.write("Power Steering Filter")
        st.subheader("$5")
        st.number_input("How much",min_value=0,max_value=100,step=1,key="filter5")
        
elif st.session_state.page == "fittings":
    st.write("#")
    st.title("Fittings")
    
    
    columns = st.columns(4)
    with columns[0]:
        st.image(air_condition_fittings)
        st.write("Air Conditioning Fittings")
        st.subheader("$1")
        st.number_input("How much",max_value=100,min_value=1,step=1,key="fittings1")
        
    with columns[1]:
        st.image(low_medium_pressure_fittings,width=500 )
        st.write("Low Medium Pressure Fittings")
        st.subheader("$1")
        st.number_input("How much",max_value=100,min_value=1,step=1,key="fittings2")
         
    with columns[2]:
        st.image(air_coupling_fittings)
        st.write("Air Coupling Fittings")
        st.subheader("$1")
        st.number_input("How much",max_value=100,min_value=1,step=1,key="fittings3")   
         
    with columns[3]:
        st.image(coolant_coupling_fittings)  
        st.write("Coolant Coupling Fittings   $1/Piece")
        st.subheader("$1")
        st.number_input("How much",max_value=100,min_value=1,step=1,key="fittings4")
        
    with columns[0]:
        st.image(workshop_coupling_fittings,width=150)
        st.write("Workshop  Coupling  Fittings")
        st.subheader("$1")
        st.number_input("How much",max_value=100,min_value=1,step=1,key="fittings5")
    with columns[1]:
        st.image(hardware,width=220)
        st.write("Hardware Fittings")
        st.subheader("$1")
        st.number_input("How much",max_value=100,min_value=1,step=1,key="fittings6")
    with columns[2]:
        st.image(hydraulic,width=150)
        st.write("Hydraulic Coupling Fittings")
        st.subheader("$1")
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
                    





































































