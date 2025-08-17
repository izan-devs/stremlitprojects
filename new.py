import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime

st.set_page_config(layout='wide')
if "page" not in st.session_state:
    st.session_state.page = "home"
tabs = st.tabs(["Home"])
def go_air_filter():
    st.session_state.page = "airfilter"
def go_hydraulic():
    st.session_state.page = "hydraulic"
def go_hardware():
    st.session_state.page = "hardware" 
def go_coolant_fittings():
    st.session_state.page = "coolant"
def go_coupling_fittings():
    st.session_state.page = "coupling"
def go_low_medium():
    st.session_state.page = "low_medium"
def go_engine():
    st.session_state.page = "engine"
def go_batteries():
    st.session_state.page = "batteries"
def go_suspension():
    st.session_state.page = "suspension"
def go_filter():
    st.session_state.page = "filter"
def go_fittings():
    st.session_state.page = "fittings"

def go_home():

    st.session_state.page = "home"

def go_contact():
    st.session_state.page = "contact"
def go_air():
    st.session_state.page = "air"
def go_workshop():
    st.session_state.page = "workshop"
oval = ""    
conical = "https://www.edelbrock.com/media/catalog/product/0/4/043613_v1.jpg?width=265&height=265&store=default&image-type=image"    
wrap = "https://i.ebayimg.com/00/s/MTUwMFgxNTAw/z/t8MAAeSwEA5ojk7S/$_12.JPG?set_id=880000500F"    
pre = "https://lirp.cdn-website.com/9a232ab5/dms3rep/multi/opt/Air_Precleaners_for_Haul_Trucks-1920w.jpg"    
filters_kit = "https://m.media-amazon.com/images/I/81LW1twN3yL._UF1000,1000_QL80_.jpg"   
diesel = "https://media.napacanada.com/is/image/GenuinePartsCompany/316436?fmt=jpg&qlt=70"    
crankcake = "https://fortnine.ca/media/catalog/product/cache/a2bf45e9635ff86c8c09fbc84b193941/catalogimages/k-and-n/universal-crankcase-vent-filter-3-4-flange-62-1360.jpg"    
gas = "https://www.walkerfiltration.com/wp-content/uploads/2019/08/Walker-Filtration-Compressed-Air-Alternative-Elements-Range-3-500x500_compressed.jpg"    
air_oil = "https://lirp.cdn-website.com/e085d07a/dms3rep/multi/opt/photo+2-21804d75-640w.jpg"    
air_filtration = "https://www.aemintakes.com/media/images/l/AEM-21-2258DK.jpg"    
hydraulic_filter = "https://i5.walmartimages.com/asr/9c432101-8f97-4260-ab97-89e3a96b9744.558dec79f2288c16db827a5812acdefe.jpeg"    
engine_oil = "https://m.media-amazon.com/images/I/61skTRhfJlL._UF1000,1000_QL80_.jpg"    
annoying = "https://image.vevor.com/us%2F71500YYRGJSJ00001V0%2Fgoods_img-v8%2Fac-hose-crimper-m100-1.2.jpg?timestamp=1644483306000"    
seal = "https://cdn.greenlinehose.com/images/full/pulsar/8.Accessories/HKIT-SCP-BSEAL.jpg"    
high = "https://www.swagelok.com/assets/images/product_images/large/SS-4-SAE-7-4.jpg?impolicy=product"    
sae = "https://m.media-amazon.com/images/I/51vFHMUFHaL._UF1000,1000_QL80_.jpg"    
quickdisconnect = "https://www.industrialspec.com/shop/media/catalog/category/40cb_series.jpg_1.png"    
power_crimp = "https://cdn.greenlinehose.com/images/full/pulsar/2.Crimp/4200.jpg"    
other_hydraulic = "https://www.powerdrives.com/wp-content/uploads/2019/1/Dixon-pneumatic-quick-disconnects.png"    
megacrimp = "https://www.southcott.com.au/images/thumbs/0001945_megacrimp-straight-male-npt-swivel_360.jpeg"   
c14 = "https://gates.scene7.com/is/image/gates/c14-sta-b-g40461-1-ang-r?id=KPYqi0&fmt=jpg&dpr=off&fit=constrain,1&wid=352&hei=276"    
global_spiral = "https://s.alicdn.com/@sc04/kf/H3ea18f9d365640a0877deffd5581b9b4v.jpg"    
fitting_for_copper_tube = "https://m.media-amazon.com/images/I/81+-d8t4UxL.jpg"    
field = "https://www.parker.com/content/dam/Parker-com/Online/Product-Images/Hose-Products-Division/zoom_1000x1000/30182_1000x1000.jpg"    
drain = "https://cdn.rona.ca/images/73455174_L.jpg"    
ball_valve = "https://m.media-amazon.com/images/I/81UIHhRxHVL.jpg"
tap = "https://m.media-amazon.com/images/I/61dQu9RYShL.jpg"  
metal = "https://www.swagelok.com/assets/images/product_images/large/SS-8-VCR-P.jpg?impolicy=superZoom"    
bundle_clamps = "https://media.napacanada.com/is/image/GenuinePartsCompany/3046690?fmt=jpg&qlt=70"    
tool_adaptor = "https://m.media-amazon.com/images/I/51TgXTg42mL._UF894,1000_QL80_.jpg"    
push_type_nylon = "https://usp.imgix.net/catalog/images/products/100/400/25145p.jpg?w=152&dpr=2&fit=max&auto=compress,format"    
push_type = "https://www.thepneumaticstore.com/images/tnImages/fittings/tn_PE.jpg"    
modular = "https://cdn1.bigcommerce.com/s-1qmaqa25jp/images/stencil/500x659/products/21414/85693/70863_1__36496.1744616881.jpg?c=1"    
hose_coupler_adapter = "https://www.swagelok.com/assets/images/product_images/large/B-6-HC-1-8.jpg?impolicy=product"    
grease = "https://www.grmflow.com/wp-content/uploads/2019/07/PlugValve-300px-1.jpg"    
compression_brass = "https://www.multipipe.co.uk/wp-content/uploads/2024/10/166230-16-x-15-Cu-Straight-Copper-Compression.jpg"    
brass = "https://www.ontariobeerkegs.com/assets/images/brass-barb-3-8-1-2-f-2.jpg"    
air_hose = "https://www.parker.com/content/dam/Parker-com/Online/Product-Images/Quick-Coupling-Division/zoom_1000x1000/70Series_zm.jpg"    
quick = "https://i5.walmartimages.com/asr/4a8ea0fe-62bc-470e-b463-50a97e137a23.4919003abb0cbab8c74dbac9e966d421.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF"    
three_way_connector = "https://s.alicdn.com/@sc04/kf/Hc6216fa757b64817b499e5ee731e75bO.jpg"    
two_way_connector = "https://kent.ca/media/catalog/product/cache/ae515196f1ace26aad3b1b066626b4f5/1/0/1027872_3.jpg"    
other = "https://m.media-amazon.com/images/I/71dfnkZdkiL.jpg"    
compression_fittings = "https://m.media-amazon.com/images/I/7100sT3bxEL._UF1000,1000_QL80_.jpg"    
bolt = "https://pim.wurth.ca/Product/8841495B-D.jpg"    
hose = "https://cdn.greenlinehose.com/images/large/fittings/8.Truck/G4316G.jpg"    
nylon_tube = "https://m.media-amazon.com/images/I/51pRjaXBHkL.jpg"    
fields_kit = "https://southernindustrial.store/wp-content/uploads/2022/12/ABFR-KIT-1-PC-1-300x240.jpg"    
air_brake = "https://southernindustrial.store/wp-content/uploads/2022/12/PC1462-10-A2d-300x240.jpg"    
coupling_fitting = "https://southernindustrial.store/wp-content/uploads/2022/12/PC1468-4A-A2b-300x240.jpg"    
vaccum_connector = "https://www.agscompany.com/cdn/shop/products/PRF-35B_823x.jpg?v=1660842351"    
push_on = "https://mobileimages.lowes.com/productimages/ce424fab-5dee-44ed-8fa1-3474c2aef646/48423962.jpg?size=pdhism"    
low_pressure = "https://www.tenaquip.com/images/large/y/ya558_lr.jpg?1556578809"    
polar = "https://m.media-amazon.com/images/I/61i8WOa5kcL.jpg"   
ac = "https://m.media-amazon.com/images/I/71ObvlbsF+L.jpg"    
manuli_fittings = "https://www.camthorne.co.uk/wp-content/uploads/2022/03/manuli-bsp-straight-male-fittings.jpg"    
crimper_tool = "https://www.zoro.com/static/cms/product/full/Z-pM6tlcpEx_.JPG"    
compresser_manifold = "https://products.atcoproductsinc.com/Asset/a1033.jpg"    
components_accessories = "https://www.componenthardware.com/images/thumbs/0000260_cross-brace-fittings_370.jpeg"    
burgaclip = "https://www.mastercoolparts.com/wp-content/uploads/2019/02/44-7159.jpg"    
block_off_adaptor = "https://i5.walmartimages.com/asr/7b5344c6-3c6b-4fe2-a78d-e007d40d589e.cd06a531e88bdeec341927339cc54c5e.jpeg"    
adaptor_port = "https://www.parker.com/content/dam/Parker-com/Online/Product-Images/Fluid-System-Connectors-Division/zoom_1000x1000/ISO_222P_X_MIX_zm.jpg"    
adaptor_pad_fitting = "https://m.media-amazon.com/images/I/71v-cznPZnL._UF350,350_QL80_.jpg"    
adaptor = "https://m.media-amazon.com/images/I/61PKv-pnWZL.jpg"    
EZ_clip = "https://cdn1.bigcommerce.com/s-xovjmui41g/images/stencil/500x659/products/2482/5330/347128__05586.1743679481.jpg?c=1"    
standard_fitting = "https://cdn1.bigcommerce.com/s-xovjmui41g/images/stencil/1280x1280/products/934/2393/354100__27720.1728678234.jpg?c=1"    
beadlock_fitting = "https://i.ebayimg.com/images/g/SrAAAOSwuB1gOYSE/s-l400.jpg"        
cabin_filter = "https://www.xtremediesel.com/mm5/graphics/00000001/VF2065_KN-1_600x600.jpg"    
power = "https://m.media-amazon.com/images/I/71Cn2FAdxcL._UF350,350_QL50_.jpg"
transmission = "https://www.duallane.com/media/catalog/product/cache/a95e9d2b539204ab79c900aa251ba8eb/f/l/fleetguard-transmission-filter-hf28943.1.jpg"
water = "https://m.media-amazon.com/images/I/51NWojSF3tL.jpg"
feul = "https://cdn1.bigcommerce.com/s-26lddf/images/stencil/1280x1280/products/4673/19637/P551337__81487.1735036382.jpg?c=2"
air = "https://5.imimg.com/data5/AN/PC/MY-2352124/truck-air-filter-500x500.jpg"
hydraulic = "https://m.media-amazon.com/images/I/617QrwH+G+L.jpg"
hardware = "https://www.mytruckpoint.ca/cdn/shop/products/3158_v1_09022010.jpg?v=1673272610"
image = "https://www.udtrucks.com/sites/default/files/styles/hero_desktop_crop/public/2024-01/Full_lineup_2024_Website%20Hero_0.jpg?itok=PgCxZ6EX"    
workshop_coupling_fittings = "https://jacosuperiorproducts.com/cdn/shop/products/Main.png?v=161431622"    
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
    columns= st.columns([1,3,1])
    with columns[1]:
        st.image("MY LOGO2.jpg",width=1000)
    st.image(image,width=1250)
    

    columns = st.columns(4)
    with columns[0]:
        st.subheader("Suspension")
        st.image(suspension_url, caption="Suspension")
        bcol = st.columns([1,3,1])
        with bcol[1]:
            
            st.button("View more?",key="one",on_click = go_suspension)
        
            
            

    with columns[1]:
        st.subheader("Truck Fittings")
        st.image(fittings_URL, caption="Fittings")
        bcol = st.columns([1,3,1])
        with bcol[1]:
            st.button("View more",key="zero",on_click = go_fittings)

            
            
            

    with columns[2]:
        st.subheader("Oil filter")
        st.image(oil_filter_url, caption="Oil filter")
        bcol = st.columns([1,3,1])
        with bcol[1]:
            st.button("View more",key="two",on_click=go_filter)
            
            
            

    with columns[3]:
        st.subheader("Batteries")
        st.image(batteries_url, caption="Batteries")
        bcol = st.columns([1,3,1])
        with bcol[1]:
            st.button("View more",key="three",on_click = go_batteries)
            
            
            
            
            
            

    
    with columns[0]:
        st.subheader("Engine parts")
        st.image(engine_parts_url, caption="Engine parts")
        bcol = st.columns([1,3,1])
        with bcol[1]:
            st.button("View more",key="four",on_click =go_engine)
        
            
            
            
            
            
    with columns[1]:
        st.subheader("Truck Oil")
        st.image(oil_url, caption="Oil")
        bcol = st.columns([1,3,1])
        with bcol[1]:
            st.button("View more",key="five")
            
            
            
            
            
    with columns[2]:
        st.subheader("Exhaust System")
        st.image(exhaust_system_url, caption="Exhaust system")
        bcol = st.columns([1,3,1])
        with bcol[1]:
            st.button("View more",key="six")
            
            
            
            
    with columns[3]:
        st.subheader("Lightings")
        st.image(ligthing_url, caption="Lightings")
        bcol = st.columns([1,3,1])
        with bcol[1]:
            st.button("View more",key="seven")
elif st.session_state.page == "airfilter":
    columns = st.columns(4)
    with columns[0]:
        st.image(wrap)
        st.write("Air Filter Wrap")
    with columns[1]:
        st.image(conical)
        st.write("Air Filter,  Conicals") 
    with columns[2]:
        st.image(oval)
        st.write("Air Filters, Oval")       






elif st.session_state.page == "hydraulic":
    columns = st.columns(5)
    with columns[0]:
        st.write("Ball Valve")
        st.image(ball_valve,width=250)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ball1")
        
    with columns[1]:
        st.write("Drain Cock")
        st.image(drain,width=250)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ball2")
        
    with columns[2]:
        st.write("Field Attachable")
        st.image(field)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ball3")
        
    with columns[3]:
        st.write("Fittings For Copper Tube")
        st.image(fitting_for_copper_tube,width=250)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ball4")
        
    with columns[4]:
        st.write("Global Spiral")
        st.image(global_spiral,width=250)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ball5")
        
    col2 = st.columns(5)
    with col2[0]:
        st.write("Hydraulic Coupling C14")
        st.image(c14)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ball6")
        
    with col2[1]:
        st.write("Mega Crimp")
        st.image(megacrimp)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ball21")
        
    with col2[2]:
        st.write("Other Hydraulic Fittings And Adaptors")
        st.image(other_hydraulic)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ball7")
        
    with col2[3]:
        st.write("Power Crimp",width=250)
        st.image(power_crimp)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ball8")
        
    with col2[4]:
        st.write("Quick Disconnect")
        st.image(quickdisconnect)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ball9")
        
    col3 = st.columns(4)
    with col3[0]:
        st.write("SAE Flare Hydraulic Adaptor")
        st.image(sae)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ball10")
        
    with col3[1]:
        st.write("SAE To SAE - High Pressure Fittings") 
        st.image(high)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ball1")
        
    with col3[2]:
        st.write("Seal Kits And Seals")
        st.image(seal)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ball12")
        
    with col3[3]:
        st.write("Hydraulic Hose Tools And Accessories")  
        st.image(annoying)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ball13")
        submitted = st.button("Submit!")
        if submitted:
            go_contact()         



                                    


elif st.session_state.page == "hardware":
    columns = st.columns(3)
    with columns[0]:
        st.write("Bundle Clamps")
        st.image(bundle_clamps,width=300)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="bundle1")
        
    with columns[1]:
        st.write("Metal caps and plugs")
        st.image(metal,width=250)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="bundle2")
        
    with columns[2]:
        st.write("Teflon Tape And Liquid")
        st.image(tap,width=250)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="bundle3")
        submitted = st.button("Submit!")
        if submitted:
            go_contact()
        
                            



elif st.session_state.page == "workshop":
    columns = st.columns(5)
    with columns[0]:
        st.write("Air Hose Coupler")
        st.image(air_hose)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="acrw")
             
    with columns[1]:
        st.write("Brass Fitting")
        st.image(brass)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="acrw1")
        
        
    with columns[2]:
        st.write("Compression Brass (Push Type Fittings)")
        st.image(compression_brass)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="acrw2")
        
    with columns[3]:
        st.write("Grease Fitting")
        st.image(grease)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="acrw3")
        
    with columns[4]:
        st.write("Hose Coupler Adapter ")
        st.image(hose_coupler_adapter,width=250)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="acrw4")
        
    col2 = st.columns(4)
    with col2[0]:
        st.write("Modular Air line")
        st.image(modular,width=250)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="acrw5")
        
    with col2[1]:
        st.write("Push Type Fittings")
        st.image(push_type,width=250)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="acrw6")
        
    with col2[2]:
        st.write("Push Type Nylon Fittings")
        st.image(push_type_nylon,width=250)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="acrw7")
        
    with col2[3]:
        st.write("Tool Adaptor Fitting")
        st.image(tool_adaptor,width=250)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="acrw8")
        submitted = st.button("Submit!")
        if submitted:
            go_contact()                                       








elif st.session_state.page == "coolant":
    columns = st.columns(3)
    with columns[0]:
        st.write("2 Way Connector")
        st.image(two_way_connector,width=250)
        st.number_input("Amount",max_value=100,min_value=0,key="way2",step=1)
        
    with columns[1]:
        st.write("Three Way Connector")
        st.image(three_way_connector,width=250)
        st.number_input("Amount",max_value=100,min_value=0,key="way3",step=1)
        
    with columns[2]:
        st.write("Quick Lock Connector")
        st.image(quick,width=250)
        st.number_input("Amount",max_value=100,min_value=0,key="way4",step=1)
        submitted = st.button("Submit!")
        if submitted:
            go_contact()        



elif st.session_state.page == "coupling":
    columns = st.columns(4)
    with columns[0]:
        st.write("Air Brake Fitting For Copper Tube")
        st.image(coupling_fitting)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="air")
        
    with columns[1]:
        st.write("Air Brake Fittings (Push To Connect)")  
        st.image(air_brake)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="fit")
        
        
    with columns[2]:
        st.write("Air Brake Fittings - Fields Kit")
        st.image(fields_kit)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="kit")
           
    with columns[3]:
        st.write("Air Brake Fitting For Nylon Tube")
        st.image(nylon_tube,width=250)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="nylon")
          
    col2 = st.columns(4)
    with col2[0]:
        st.write("Air Brake Hose Couplings")
        st.image(hose,width=250)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="hose")
         
    with col2[1]:
        st.write("Air Brake Terminal Bolt")
        st.image(bolt,width=285)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="bolt")
          
    with col2[2]:
        st.write("Compression Fittings")
        st.image(compression_fittings,width=250)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="cf")
            
    with col2[3]:
        st.write("Other Air Couplings And Fittings")
        st.image(other,width=250)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="oacaf")
        submitted = st.button("Submit!")
        if submitted:
            go_contact()                          





elif st.session_state.page == "low_medium":
    columns = st.columns(4)
    with columns[0]:
        st.write("Other Low Pressure Fittings")
        st.image(low_pressure)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="low")
           
    with columns[1]:
        st.write("Push On 1/2 in ID")
        st.image(push_on)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="push")
             
    with columns[2]:
        st.write("Push On 1/4 in ID")
        st.image(push_on)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="on")
        
    with columns[3]:
        st.write("Push On 3/4 in ID")
        st.image(push_on)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ID")
             
    col2 = st.columns(4)
    with columns[0]:
        st.write("Push On 3/8 in ID")
        st.image(push_on)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ID2")
        
    with columns[1]:
        st.write("Push On 5/16 in ID")
        st.image(push_on)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ID3")
        
    with columns[2]:
        st.write("Push On 5/8 in ID")
        st.image(push_on)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ID4")
            
    with columns[3]:
        st.write("Vaccum Connector")
        st.image(vaccum_connector)
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="ID5")
        submitted = st.button("Submit!")
        if submitted:
            go_contact()                       





elif st.session_state.page == "air":
    columns = st.columns(5)
    with columns[0]:
        st.write("Beadlock Reduced Fittings")
        st.image(beadlock_fitting)
        st.header("$25")
        st.number_input("Amount",key="dead",max_value=100,min_value=0,step=1)
        
        
    with columns[1]:
        st.write("Beadlock Standard Fittings")
        st.image(standard_fitting)
        st.header("$25")
        st.number_input("Amount",key="standart",max_value=100,min_value=0,step=1)
        
        
    with columns[2]:
        st.write("EZ Clip Fittings")
        st.image(EZ_clip)
        st.header("$25")
        st.number_input("Amount",key="ez",max_value=100,min_value=0,step=1)
        
             
    with columns[3]:
        st.write("Adaptor Fittings")
        st.image(adaptor)
        st.header("$25")
        st.number_input("Amount",key="adaptor",max_value=100,min_value=0,step=1)
        
    with columns[4]:
        st.write("Adaptor Pad Fittings")
        st.image(adaptor_pad_fitting)
        st.header("$25")
        st.number_input("Amount",key="pad",max_value=100,min_value=0,step=1)
        
       
    col2 = st.columns(5)
    with col2[0]:
        st.write("Adaptor Port")
        st.image(adaptor_port)
        st.header("$25")
        st.number_input("Amount",key="port",max_value=100,min_value=0,step=1)
        
        
    with col2[1]:
        st.write("Block Off Adaptor")
        st.image(block_off_adaptor)
        st.header("$25")
        st.number_input("Amount",key="block",max_value=100,min_value=0,step=1)
        
          
    with col2[2]:
        st.write("BurgaClip Fittings")
        st.image(burgaclip)
        st.header("$25")
        st.number_input("Amount",key="burga",max_value=100,min_value=0,step=1)
        
          
    with col2[3]:
        st.write("Components And Accessories")
        st.image(components_accessories)
        st.header("$25")
        st.number_input("Amount",key="comp",max_value=100,min_value=0,step=1)  
        
        
    with col2[4]:
        st.write("Compressor Manifold")
        st.image(compresser_manifold)
        st.header("$25")
        st.number_input("Amount",key="compressoor",max_value=100,min_value=0,step=1)
        
          
    col3 = st.columns(4)
    with col3[0]:
        st.write("Crimper Tool")
        st.image(crimper_tool)
        st.header("$25")
        st.number_input("Amount",key="crimper",max_value=100,min_value=0,step=1)
        
        
    with col3[1]:
        st.write("Manuli Fittings")
        st.image(manuli_fittings)
        st.header("$25")
        st.number_input("Amount",key="manuli",max_value=100,min_value=0,step=1)
        
        
    with col3[2]:
        st.write("Other A/C Fittings")
        st.image(ac)
        st.header("$25")
        st.number_input("Amount",key="ac",max_value=100,min_value=0,step=1)
        
         
    with col3[3]:
        st.write("PolarSeal")
        st.image(polar)
        st.header("$25")
        st.number_input("Amount",key="seal",max_value=100,min_value=0,step=1)
        submitted = st.button("Submit!")
        if submitted:
            go_contact()
        
               

                       

elif st.session_state.page == "engine":
    st.title("Engine part")
    col1,col2 = st.columns([1,2])
    with col1:
        st.image(engine_parts_url)
    with col2:
        st.subheader("Description")
        st.write("This engine component represents a transformative enhancement, delivering a level of power that exceeds "
         "expectations, truly rendering it a formidable asset. Remarkably, it operates with minimal environmental "
         "impact, allowing for recharging and thereby reducing emissions—a boon for those traversing extensive distances. "
         "The cost is exceptionally reasonable, and shipping is provided at no additional charge. To acquire this "
         "superior component, simply select the desired quantity and proceed; you will be seamlessly directed to the "
         "purchase page, ready to secure its benefits.")

        st.header("$2.50")
        st.number_input("Amount",min_value=0,max_value=100,step=1,key="engine")  
        submitted = st.button("Submit!")
        if submitted:
            go_contact()              





elif st.session_state.page == "batteries":
    st.title("Batterie")
    col1,col2 = st.columns([1,2])
    with col1:
        st.image(batteries_url)
    with col2:
        st.subheader("Description")
        st.write("This battery is a remarkable innovation, designed to imbue your truck with renewed vitality and ensure "
         "each journey unfolds with refined smoothness. Upon installation, it does far more than merely replenish "
         "energy—it delivers an extraordinary surge of power, restoring your vehicle to readiness within moments. "
         "Such immediacy allows you to reach your destination with admirable efficiency. Remarkably, this advancement "
         "remains entirely accessible in cost, requiring only purchase, installation, and the quiet certainty that "
         "its performance will speak for itself.")

        st.header("$5")  
        st.number_input("Amount",max_value=100,min_value=0,step=1,key="batterie")
        
        submitted = st.button("Submit!")
        if submitted:
            go_contact()





elif st.session_state.page == "suspension":
    st.title("Suspension")


    col1, col2 = st.columns([1,2])  
    with col1:
        st.image(suspension_url, caption="Suspension")

    with col2:
        st.subheader("Description")
        st.write("This suspension system is an exceptional enhancement, engineered to endow your vehicle with an exquisitely "
         "smooth and composed ride. It deftly mitigates the intrusion of bumps and imperfections, ensuring the car "
         "glides with poise rather than succumbing to unruly motion. Cornering becomes a refined exercise in control, "
         "allowing one to navigate even the most uneven terrain with confidence. Constructed from resilient, "
         "high-quality materials, it promises enduring performance and a graceful longevity. Installation is "
         "straightforward, accommodating an array of vehicles. Once experienced, its transformative effect becomes "
         "undeniably apparent.")

            
        st.header("$10")
        st.number_input("Amount", key="suspension", min_value=0, max_value=100, step=1)

        
        submitted = st.button("Submit!")
        if submitted:
            go_contact()

    


elif st.session_state.page == "filter":
    st.title("FILTERS")
    col3 = st.columns(5)
    with col3 [0]:
        st.image(air)
        st.write("Air Filter")
        st.button("View",key="b1",on_click=go_air_filter)
        
    with col3[1]:
        st.image(feul)
        st.write("Feul Filter")
        st.button("View",key="b12")
        
    with col3[2]:
        st.image(water)
        st.write("Water Filters")
        st.button("View",key="b13")
        
    with col3[3]:
        st.image(transmission)
        st.write("Transmission Filter")
        st.button("View",key="b14")
        
    with col3[4]:
        st.image(power)
        st.write("Power Steering Filter")
        st.button("View",key="b15")
        
    col4=st.columns(5)
    with col4[0]:
        st.image(cabin_filter,width=250)
        st.write("Air Cabin Filter")
        st.button("View",key="b16")
        
    with col4[1]:
        st.image(engine_oil,width=250)
        st.write("Engine Oil Filters")
        st.button("View",key="b17")
    with col4[2]:
        st.image(hydraulic_filter)
        st.write("Hydraulic Filter")
        st.button("View",key="b18")
    with col4[3]:
        st.image(air_filtration)
        st.write("Air Filtration System",width=250)
        st.button("View",key="b19")
    with col4[4]:
        st.image(air_oil)
        st.write("Air Oil Seperator")
        st.button("View",key="b10")
    col2 = st.columns(5)
    with col2[0]:
        st.image(gas)
        st.write("Compressed Air And Gas Elements")
        st.button("View",key="b111")
    with col2[1]:
        st.image(crankcake)
        st.write("CrankCase Filters")    
        st.button("View",key="b112")
    with col2[2]:
        st.image(diesel,width=245)
        st.write("Diesel Exhaust Fluid Filter")
        st.button("View",key="b113")
    with col2[3]:
        st.image(filters_kit) 
        st.write("Filters Kit")
        st.button("View",key="b114")
    with col2[4]:
        st.image(pre,width=250)
        st.write("Pre Cleaner")       
        st.button("View",key="b115")


        
elif st.session_state.page == "fittings":
    st.write("#")
    st.title("Fittings")
    
    
    columns = st.columns(4)
    with columns[0]:
        st.image(air_condition_fittings,width=250)
        st.write("Air Conditioning Fittings")
        st.button("View",key="fittings1",on_click =go_air)
        
        
    with columns[1]:
        st.image(low_medium_pressure_fittings,width=250 )
        st.write("Low Medium Pressure Fittings")
        st.button("View",key="fittings2",on_click=go_low_medium)
        
         
    with columns[2]:
        st.image(air_coupling_fittings,width=250)
        st.write("Air Coupling Fittings")
        st.button("View",key="fittings3",on_click=go_coupling_fittings)  
         
    with columns[3]:
        st.image(coolant_coupling_fittings,width=250)  
        st.write("Coolant Coupling Fittings   $1/Piece")
        st.button("View",key="fittings4",on_click=go_coolant_fittings)
        
    with columns[0]:
        st.image(workshop_coupling_fittings,width=250)
        st.write("Workshop  Coupling  Fittings")
        st.button("View",key="fittings5",on_click=go_workshop)
        
    with columns[1]:
        st.image(hardware,width=250)
        st.write("Hardware Fittings")
        st.button("View",key="fittings6",on_click=go_hardware)
        
    with columns[2]:
        st.image(hydraulic,width=250)
        st.write("Hydraulic Coupling Fittings")
        st.button("View",key="fittings7",on_click=go_hydraulic)
        
        

        
        

        



elif st.session_state.page == "contact":
    st.header("Order Summary")
    
    
    engine_price = 2.50
    air_cond_price = 25  

    
    engine_quantity = st.session_state.get("engine", 0)
    beadlock1_quantity = st.session_state.get("dead", 0)
    beadlock1_quant2ty= st.session_state.get("standart", 0)
    ez_clip_quantity = st.session_state.get("ez", 0)
    adaptor_quantity = st.session_state.get("adaptor", 0)
    adaptor_pad_quantity = st.session_state.get("pad", 0)
    adaptor_port_quantity = st.session_state.get("port", 0)
    block_off_quantity = st.session_state.get("block", 0)
    burgaclip_quantity = st.session_state.get("burga", 0)
    components_accessories_quantity = st.session_state.get("comp", 0)
    compressor_manifold_quantity = st.session_state.get("compressoor", 0)
    crimper_tool_quantity = st.session_state.get("crimper", 0)
    manuli_fittings_quantity = st.session_state.get("manuli", 0)
    other_ac_fittings_quantity = st.session_state.get("ac", 0)
    polarseal_quantity = st.session_state.get("seal", 0)
    
    grand_total = 0 

    
    if engine_quantity > 0:
        total = engine_quantity * engine_price
        st.write(f"Engine: Quantity: {engine_quantity} -- Price: ${engine_price} -- Total: ${total}")
        grand_total += total

   
    if beadlock1_quantity > 0:
        total = beadlock1_quantity * air_cond_price
        st.write(f"Beadlock Reduced Fittings: Quantity: {beadlock1_quantity} -- Price: ${air_cond_price} -- Total: ${total}")
        grand_total += total

    if  beadlock1_quant2ty> 0:
        total = beadlock1_quant2ty * air_cond_price
        st.write(f"Beadlock Standard Fittings: Quantity: {beadlock1_quant2ty} -- Price: ${air_cond_price} -- Total: ${total}")
        grand_total += total

    if ez_clip_quantity > 0:
        total = ez_clip_quantity * air_cond_price
        st.write(f"Air Conditioning Fittings 3: Quantity: {ez_clip_quantity} -- Price: ${air_cond_price} -- Total: ${total}")
        grand_total += total

    if adaptor_quantity > 0:
        total = adaptor_quantity * air_cond_price
        st.write(f"Air Conditioning Fittings 4: Quantity: {adaptor_quantity} -- Price: ${air_cond_price} -- Total: ${total}")
        grand_total += total

    if adaptor_pad_quantity > 0:
        total = adaptor_pad_quantity * air_cond_price
        st.write(f"Air Conditioning Fittings 5: Quantity: {adaptor_pad_quantity} -- Price: ${air_cond_price} -- Total: ${total}")
        grand_total += total

    if adaptor_port_quantity > 0:
        total = adaptor_port_quantity * air_cond_price
        st.write(f"Air Conditioning Fittings 6: Quantity: {adaptor_port_quantity} -- Price: ${air_cond_price} -- Total: ${total}")
        grand_total += total

    if block_off_quantity > 0:
        total = block_off_quantity * air_cond_price
        st.write(f"Air Conditioning Fittings 7: Quantity: {block_off_quantity} -- Price: ${air_cond_price} -- Total: ${total}")
        grand_total += total
    if burgaclip_quantity > 0:
        total = burgaclip_quantity * air_cond_price
        st.write(f"BurgaClip Fittings: Quantity: {burgaclip_quantity} -- Price: ${air_cond_price} -- Total: ${total}")
        grand_total += total

    if components_accessories_quantity > 0:
        total = components_accessories_quantity * air_cond_price
        st.write(f"Components And Accessories: Quantity: {components_accessories_quantity} -- Price: ${air_cond_price} -- Total: ${total}")
        grand_total += total

    if compressor_manifold_quantity > 0:
        total = compressor_manifold_quantity * air_cond_price
        st.write(f"Compressor Manifold: Quantity: {compressor_manifold_quantity} -- Price: ${air_cond_price} -- Total: ${total}")
        grand_total += total

    if crimper_tool_quantity > 0:
        total = crimper_tool_quantity * air_cond_price
        st.write(f"Crimper Tool: Quantity: {crimper_tool_quantity} -- Price: ${air_cond_price} -- Total: ${total}")
        grand_total += total

    if manuli_fittings_quantity > 0:
        total = manuli_fittings_quantity * air_cond_price
        st.write(f"Manuli Fittings: Quantity: {manuli_fittings_quantity} -- Price: ${air_cond_price} -- Total: ${total}")
        grand_total += total

    if other_ac_fittings_quantity > 0:
        total = other_ac_fittings_quantity * air_cond_price
        st.write(f"Other A/C Fittings: Quantity: {other_ac_fittings_quantity} -- Price: ${air_cond_price} -- Total: ${total}")
        grand_total += total

    if polarseal_quantity > 0:
        total = polarseal_quantity * air_cond_price
        st.write(f"PolarSeal: Quantity: {polarseal_quantity} -- Price: ${air_cond_price} -- Total: ${total}")
        grand_total += total
    
    if grand_total > 0:
        st.subheader(f"Grand Total: ${grand_total}")
    else:
        st.write("No items purchased yet.")
    
    st.title("Customer Details")
    
    

    st.set_page_config(page_title="Local Orders", page_icon="🧾")

    # --- Where to store the CSV ---
    DATA_DIR = Path(__file__).parent / "data"
    DATA_DIR.mkdir(exist_ok=True)
    CSV_PATH = DATA_DIR / "orders.csv"

    def append_order(order: dict):
        """Append a single order to CSV, creating headers if file doesn't exist."""
        df = pd.DataFrame([order])
        df.to_csv(
            CSV_PATH,
            mode="a",
            header=not CSV_PATH.exists(),
            index=False,
            encoding="utf-8",
        )



    # Keep transient counters or UI state in session_state (not strictly required here)
    if "orders_saved" not in st.session_state:
        st.session_state.orders_saved = 0

    # --- Form: only writes when the user clicks Submit ---
    with st.form("order_form", clear_on_submit=True):
        customer = st.text_input("Customer name")
        email = st.text_input("email")
        phone = st.text_input("Phone Number")
        Additional_comments = st.text_area("Notes (optional)")
        submitted = st.form_submit_button("Place order")

    if submitted:
        # Minimal validation
        if not customer or not email:
            st.error("Please fill in customer and product.")
        else:
            order = {
                "customer": datetime.utcnow().isoformat(timespec="seconds"),
                "email": customer.strip(),
                "phone": email.strip(),
                "additional comments": int(phone),
                
            }
            append_order(order)
            st.session_state.orders_saved += 1
            st.success("✅ Order saved to CSV.")

    # --- Preview & Download ---
    st.divider()
    st.subheader("Saved orders")
    if CSV_PATH.exists():
        st.caption(f"Saved at: `{CSV_PATH}`")
        st.dataframe(pd.read_csv(CSV_PATH))
        st.download_button(
            "Download orders.csv",
            data=CSV_PATH.read_bytes(),
            file_name="orders.csv",
            mime="text/csv",
        )
    else:
        st.info("No orders saved yet.")

    st.caption("Tip: run with `streamlit run app.py`")

    


