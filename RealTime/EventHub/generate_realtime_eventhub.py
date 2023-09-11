## dbr library:
#com.datastax.spark:spark-cassandra-connector-assembly_2.12:3.2.0   to connect spark with cassandra
#com.microsoft.azure:azure-eventhubs-spark_2.12:2.3.22   to connect spark with event hub
#datastax:spark-cassandra-connector:2.4.0-s_2.11   to connect cassandra
import random
import psutil

import os
import socket
import json
from azure.eventhub import EventHubProducerClient, EventData
import time
from datetime import datetime
event_hub_connection_string = 'Endpoint=sb://eventhuboperation.servicebus.windows.net/;SharedAccessKeyName=policy_1;SharedAccessKey=g1SC+MOi33ABC+z3jDv0V8P5eiMAdoAAN+AEhBgAVt8=;EntityPath=e_operation'
event_hub_name = 'e_operation'

# Create a producer client to produce and publish events to the event hub.

producer = EventHubProducerClient.from_connection_string(conn_str=event_hub_connection_string, eventhub_name=event_hub_name)
Cust='LUC'
Project_ID='LUC-01'
BatchID = 1
Aeration_rate=42.0
Agitator_RPM=100.0
Acid_flow_rate=30.0
Base_flow_rate=0.0
Heating_cooling_water_flow_rate=56.335
Heating_water_flow_rate=251.75
Air_head_pressure=0.0001
Dumped_broth_flow=11.3
Vessel_Weight=11.3
Generated_heat=11.3
carbon_dioxide_percent_in_off_gas=11.3
PAA_flow=11.3
PAA_concentration_offline=11.3
Oil_flow=11.3
NH_3_concentration_off_line=11.3
Oxygen_Uptake_Rate=11.3
Oxygen_in_percent_in_off_gas=11.3
Offline_Penicillin_concentration=11.3
Offline_Biomass_concentratio=11.3
Carbon_evolution_rate=11.3
Ammonia_shots=11.3
Viscosity=11.3
Fault_reference=11.3
Recipe_driven_1=11.3
No_Raman_spec=11.3
Raman_spec_recorded=11.3
Batch_reference=11.3
Fault_flag=11

try:
    while True:
        event_data_batch = producer.create_batch() # Create a batch. You will add events to the batch later.       
        Substrate_concentration=0.0020703 + 0.001*random.random()
        Sugar_feed_rate=170 + random.randint(5,10)
        Temperature = 290 + random.randint(5,10)
        Water_for_injection_dilution = 250.0 + random.randint(0,10)
        Dissolved_oxygen_concentration = 13+random.random()
        Vessel_Volume = 52671+random.randint(12671, 22671)
        pH = 5+random.random()

        #Penicillin_concentration = 0+random.random()
        #reading = {'Customer': customer,'Testcampaing': test_campaing,'Test_id': test_id,'hostname': hostname, 'timestamp': str((datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")), 'Sugar_mass_flow':Sugar_mass_flow,'Water_injection':Water_injection,'Temperature':Temperature,'DO2':DO2,'Vessel_volume':Vessel_volume,'pH':pH}
        
        reading = {'Cust': Cust,'Project_ID': Project_ID,'BatchID': BatchID,'Time (h)': datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),"Aeration rate(Fg:L/h)":Aeration_rate,"Agitator RPM(RPM:RPM)":Agitator_RPM,"Sugar feed rate(Fs:L/h)":Sugar_feed_rate,"Acid flow rate(Fa:L/h)":Acid_flow_rate,"Base flow rate(Fb:L/h)":Base_flow_rate,"Heating/cooling water flow rate(Fc:L/h)":Heating_cooling_water_flow_rate,
        "Heating water flow rate(Fh:L/h)":Heating_water_flow_rate,"Water for injection/dilution(Fw:L/h)":Water_for_injection_dilution,
        "Air head pressure(pressure:bar)":Air_head_pressure,"Dumped broth flow(Fremoved:L/h)":Dumped_broth_flow,
        "Substrate concentration(S:g/L)":Substrate_concentration,"Dissolved oxygen concentration(DO2:mg/L)":Dissolved_oxygen_concentration,
        "Vessel Volume(V:L)":Vessel_Volume,"Vessel Weight(Wt:Kg)":Vessel_Weight,"pH(pH:pH)":pH,"Temperature(T:K)":Temperature,"Generated heat(Q:kJ)":Generated_heat,
        "carbon dioxide percent in off-gas(CO2outgas:%)":carbon_dioxide_percent_in_off_gas,"PAA flow(Fpaa:PAA flow (L/h))":PAA_flow,"PAA concentration offline(PAA_offline:PAA (g L^{-1}))":PAA_concentration_offline,
        "Oil flow(Foil:L/hr)":Oil_flow,"NH_3 concentration off-line(NH3_offline:NH3 (g L^{-1}))":NH_3_concentration_off_line,"Oxygen Uptake Rate(OUR:(g min^{-1}))":Oxygen_Uptake_Rate,"Oxygen in percent in off-gas(O2:O2  (%))":Oxygen_in_percent_in_off_gas,"Offline Penicillin concentration(P_offline:P(g L^{-1}))":Offline_Penicillin_concentration,
        "Offline Biomass concentratio(X_offline:X(g L^{-1}))":Offline_Biomass_concentratio,"Carbon evolution rate(CER:g/h)":Carbon_evolution_rate,"Ammonia shots(NH3_shots:kgs)":Ammonia_shots,"Viscosity(Viscosity_offline:centPoise)":Viscosity,"Fault reference(Fault_ref:Fault ref)":Fault_reference,"0 - Recipe driven 1 - Operator controlled(Control_ref:Control ref)":Recipe_driven_1,
        "1- No Raman spec":No_Raman_spec," 1-Raman spec recorded": Raman_spec_recorded,"Batch reference(Batch_ref:Batch ref)":Batch_reference,"Fault flag":Fault_flag}

        #reading = {'Sugar_mass_flow':Sugar_mass_flow,'Water_injection':Water_injection,'Temperature':Temperature,'DO2':DO2,'Vessel_volume':Vessel_volume,'pH':pH}

        s = json.dumps(reading) # Convert the reading into a JSON string.
        print(s)
        event_data_batch.add(EventData(s)) # Add event data to the batch.
        producer.send_batch(event_data_batch)
        import time
        time.sleep(2) #delate every 10s
except KeyboardInterrupt:
    #pass
    producer.close()
    
