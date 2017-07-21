'''
Card Data Constants
'''
COLORS = ['White', 'Blue', 'Black', 'Red', 'Green']
COLOR_MAP = {'White': 'W', 'Blue':'U', 'Black':'B', 'Red':'R', 'Green':'G'}
RARITIES = ['Common', 'Uncommon', 'Rare', 'Mythic Rare', 'Basic', 'Special']
COLORID_POSSIBLE = ['C', 'W', 'U', 'B', 'R', 'G', 
					'WU', 'WB', 'WR', 'WG', 'UB', 'UR', 'UG', 'BR', 'BG', 'RG', 
					'WUB', 'WUR', 'WUG', 'WBR', 'WBG', 'WRG', 'UBR', 'UBG', 'URG', 'BRG', 
					'WUBR', 'WUBG', 'WURG', 'WBRG', 'UBRG', 
					'WUBRG']

'''
Set Code Constants
'''
CORE_SETS = ['LEA', 'LEB', '2ED', '3ED', '4ED', '5ED', '6ED', '7ED', '8ED',
			 '9ED','10E', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'ORI']

EXPANSION_SETS = ['ARN', 'ATQ', 'LEG', 'DRK', 'FEM', 'HML', 'ICE', 'ALL', 
				  'CSP', 'MIR', 'VIS', 'WTH', 'TMP', 'STH', 'EXO', 'USG',
				  'ULG', 'UDS', 'MMQ', 'NMS', 'PCY', 'INV', 'PLS', 'APC',
				  'ODY', 'TOR', 'JUD', 'ONS', 'LGN', 'SCG', 'MRD', 'DST',
				  '5DN', 'CHK', 'BOK', 'SOK', 'RAV', 'GPT', 'DIS', 'TSP',
				  'TSB', 'PLC', 'FUT', 'LRW', 'MOR', 'SHM', 'EVE', 'ALA',
				  'CON', 'ARB', 'ZEN', 'WWK', 'ROE', 'SOM', 'MBS', 'NPH',
				  'ISD', 'DKA', 'AVR', 'RTR', 'GTC', 'DGM', 'THS', 'BNG',
				  'JOU', 'KTK', 'FRF', 'DTK', 'BFZ', 'OGW', 'SOI', 'EMN',
				  'KLD', 'AER', 'AKH', 'HOU']

STARTER_SETS = ['POR', 'PO2', 'PTK', 'S99', 'S00', 'ITP', 'RQS', 'W16', 'W17']

COMPILATION_SETS = ['CHR', 'MED', 'ME2', 'ME3', 'ME4', 'DPA', 'ARC', 
					'MMA', 'VMA', 'TPR', 'MM2', 'EXP', 'PZ1', 'W16', 
					'EMA', 'PZ2', 'MM3', 'W17', 'MPS']

NONSTANDARD_SETS = ['HOP', 'PC2', 'CMD', 'C13', 'C14', 'C15', 'C16',
					'CNS', 'CN2', 'CM1']

NONTOURNAMENT_SETS = ['CED', 'CEI', 'UGL', 'UNH']

ONLINE_SETS = ['MED', 'ME2', 'ME3', 'TD0', 'ME4', 'VMA', 'TPR', 'PZ1', 'PZ2']

PROMO_SETS = ['p2HG', 'pWOR', 'pWOS', 'pLGM', 'pPRE', 'pPRO', 'pREL', 'pMPR',
			  'pCMP', 'pARL', 'pGTW', 'pWPN', 'pDRC', 'pJGP', 'pMEI', 'p15A',
			  'pFNM', 'pELP', 'pALP', 'pLPA', 'pMGD', 'pGPX', 'pSUS', 'pGRU',
			  'pSUM', 'pWCQ', 'pHHO', 'pPOD', 'FRF_UGIN', 'pCEL']

MISC_SETS = ['VAN','CST','MD1','MGB']

BOX_SETS = ['ATH', 'BRB', 'BTD', 'DKM', 'EVG', 'DRB', 'DD2' , 'DDC', 'TD0', 'V09',
			'DDD', 'DDE', 'H09', 'DPA', 'V10', 'DDF', 'DDG', 'TD0', 'PD2', 
			'CMD', 'V11', 'DDH', 'PD3', 'DDI', 'V12', 'DDJ', 'CM1', 'TD2',
			'DDK', 'V13', 'DDL', 'C13', 'MD1', 'V14', 'DDN', 'C14', 'DD3',
			'DDO', 'V15', 'DDP', 'C15', 'DDQ', 'V16', 'DDR', 'C16', 'PCA',
			'DDS', 'CMA', 'PCA']

SUPPLEMENTAL_SETS = ['HOP', 'ARC', 'PC2', 'CNS', 'CN2', 'E01']

PLANECHASE_SETS = ['HOP', 'PC2', 'PCA']

COMMANDER_SETS = ['CMD', 'CM1', 'C13', 'C14', 'C15', 'C16', 'CMA']

ARCHENEMY_SETS = ['ARC', 'E01']

CONSPIRACY_SETS = ['CNS', 'CN2']

WELCOMEDECK_SETS = ['W16', 'W17']

UN_SETS = ['UGL', 'UNH']

DUELDECK_SETS = ['EVG', 'DD2', 'DDC', 'DDD', 'DDE', 'DDF', 'DDG', 'DDH', 'DDI',
				 'DDJ', 'TD2', 'DDK', 'DDL', 'DDM', 'DDN', 'DD3', 'DDO', 'DDP',
				 'DDQ', 'DDR', 'DDS']

FTV_SETS = ['DRB', 'V09', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16']

MASTERS_SETS = ['MED', 'ME2', 'ME3', 'ME4', 'MMA', 'VMA', 'TPR', 'MM2', 'EMA', 'MM3']

ALL_SETS = ['LEA', 'LEB', 'CED', 'CEI', '2ED', 'ARN', 'pDRC', 'ATQ', '3ED', 
			'LEG', 'DRK', 'FEM', 'pLGM', 'pMEI', '4ED', 'ICE', 'CHR', 'HML', 
			'ALL', 'RQS', 'pARL', 'pCEL', 'MIR', 'MGB', 'ITP', 'VIS', '5ED', 
			'VAN', 'POR', 'pPOD', 'WTH', 'pPRE', 'TMP', 'STH', 'PO2', 'pJGP', 
			'EXO', 'UGL', 'pALP', 'USG', 'ATH', 'ULG', '6ED', 'PTK', 'UDS', 
			'S99', 'pGRU', 'pWOR', 'pWOS', 'MMQ', 'BRB', 'pSUS', 'pFNM', 'pELP', 
			'NMS', 'S00', 'PCY', 'BTD', 'INV', 'PLS', '7ED', 'pMPR', 'APC', 
			'ODY', 'DKM', 'TOR', 'JUD', 'ONS', 'LGN', 'SCG', 'pREL', '8ED', 
			'MRD', 'DST', '5DN', 'CHK', 'UNH', 'BOK', 'SOK', '9ED', 'RAV', 
			'p2HG', 'pGTW', 'GPT', 'pCMP', 'DIS', 'CSP', 'CST', 'TSB', 'TSP', 
			'pHHO', 'PLC', 'pPRO', 'pGPX', 'FUT', '10E', 'pMGD', 'pSUM', 'MED', 
			'LRW', 'EVG', 'MOR', 'pLPA', 'p15A', 'SHM', 'EVE', 'DRB', 'ME2', 
			'pWPN', 'ALA', 'DD2', 'CON', 'DDC', 'ARB', 'M10', 'V09', 'HOP', 
			'ME3', 'ZEN', 'DDD', 'H09', 'WWK', 'DDE', 'ROE', 'DPA', 'ARC', 'M11', 
			'V10', 'DDF', 'SOM', 'PD2', 'ME4', 'MBS', 'DDG', 'NPH', 'CMD', 'M12', 
			'V11', 'DDH', 'ISD', 'PD3', 'DKA', 'DDI', 'AVR', 'PC2', 'M13', 'V12', 
			'DDJ', 'RTR', 'CM1', 'GTC', 'DDK', 'DDS', 'pWCQ', 'DGM', 'MMA', 'M14', 
			'V13', 'DDL', 'THS', 'C13', 'BNG', 'DDM', 'JOU', 'MD1', 'CNS', 'VMA', 
			'CPK', 'M15', 'V14', 'DDN', 'KTK', 'C14', 'DD3_GVL', 'DD3_DVD', 'DD3_EVG', 
			'DD3_JVC', 'FRF_UGIN', 'FRF', 'DDO', 'DTK', 'TPR', 'MM2', 'ORI', 'V15', 
			'DDP', 'EXP', 'BFZ', 'C15', 'OGW', 'DDQ', 'W16', 'SOI', 'EMA', 'EMN', 
			'V16', 'CN2', 'DDR', 'MPS', 'KLD', 'C16', 'PCA', 'AER', 'MM3', 'W17', 
			'MPS_AKH', 'AKH', 'CMA', 'E01', 'HOU']