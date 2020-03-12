'''
Basic information
'''

model_list=['WRF_OXF', #WRF with Morrison 2mom microphysics run by University of Oxford
            'WRF_NASA', #NU-WRF with P3 microphysics run by NASA GISS/Goddard
            'RAMS_CSU', #RAMS run by Colorado State University
            'COSMO_KIT', #COSMO run by KIT Karlsruhe
            'UM_LEEDS', #Unified Model run by University of Leeds
            'MesoNH_Toulouse', #MesoNH run by Meteo France Toulouse
            'WRF_PNNL' # WRF with spectral bin microphysics run by PNNL
             ]

case_list=['CLN', # "Clean case" with surface (500)
           'POL'
           ]
dt_list=['1h', # 1 hour resolution, avaliable for all three domains for the entire simulation period (... - ... UTC)
         '5m', # 1 minute time resolution, avaliable in inner domain (500m) for ... - ... UTC
         '1m' # 1 minute time resolution, avaliable in inner domain (500m) for ... - ...  UTC
        ]
dx_list=['4500m', #outer domain (D1) with 4.5 km resolution availabe at 1h resolution
         '1500m', #outer domain (D1) with 4.5 km resolution availabe at 1h resolution
         '500m', #outer domain (D1) with 4.5 km resolution availabe at all resolutions
         ]
