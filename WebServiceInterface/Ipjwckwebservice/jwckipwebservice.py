from suds.client import Client
# from base64test import base64demo as b64
# from readfilexml import readfile
# from SublimeTest.readfile import readfile as rd
class ckwwebservicecloud:
	def __init__(self,client):
		self.client=client

	def cxBdcQL(self):
		# bhdm=''
		arg0='PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjxVU0VSTUFSS0VSPjxDT05ESVRJT04+PFVTRVJOQU1FPlNWQXdNREF3TURNPTwvVVNFUk5BTUU+PFBBU1NXT1JEPk1USXo8L1BBU1NXT1JEPjwvQ09ORElUSU9OPjwvVVNFUk1BUktFUj4NCg=='
		
		result=self.client.service.cxBdcQL(arg0)
		print(result)

	def feedBdcQL(self):
		arg0='PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjxVU0VSTUFSS0VSPjxDT05ESVRJT04+PFVTRVJOQU1FPlNWQXdNREF3TURNPTwvVVNFUk5BTUU+PFBBU1NXT1JEPk1USXo8L1BBU1NXT1JEPjwvQ09ORElUSU9OPjwvVVNFUk1BUktFUj4NCg=='
		arg1='PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjxNZXNzYWdlPjxIZWFkPjxDUkVBVEVUSU1FPk1qQXhOaTB3Tmkwd015QXdPVG94TVRveU5BPT08L0NSRUFURVRJTUU+PFJFU1BPTlNFQ09ERT5NREF3TUE9PTwvUkVTUE9OU0VDT0RFPjxSRVNQT05TRUlORk8+PC9SRVNQT05TRUlORk8+PERJR0lUQUxTSUdOIG5hbWU9IjVwV3c1YTJYNTYyKzVaQ04iPjwvRElHSVRBTFNJR04+PC9IZWFkPjxEYXRhPjxCRENGS0xJU1Q+PEJEQ0NYSkcgbmFtZT0iNUxpTjVZcW81THFuNXArbDZLK2k1N3VUNXA2YyI+PENYUVFESD5RVEU1TURZeE1UUTJNREF3TURFd01EQXdNREV4Tnc9PTwvQ1hRUURIPjxSRVNVTFQ+TURBd01BPT08L1JFU1VMVD48VERTWVFMSVNUPjxURFNZUSBuYW1lPSI1WnlmNVp5dzVvbUE1cHlKNXAyRCI+PEJEQ0RZSD5NVE13TVRBeU1ERXlNREl6U2tFd01EQXdNVmN3TURBd01EQXdNUT09PC9CRENEWUg+PFpMPlFlVzRna1BsakxwRTVwMlI8L1pMPjxaRE1KPk9USTVORE11TmpZPTwvWkRNSj48TUpEVz5NZz09PC9NSkRXPjxZVD5Ndz09PC9ZVD48UUxMWD5NUT09PC9RTExYPjxRTFhaPk1UQXc8L1FMWFo+PEJEQ1FaSD5Xa2d4TWpNME5qVTNPRGs9PC9CRENRWkg+PERKSkc+U1ZBd01EQXdNdz09PC9ESkpHPjxZV0g+TkRZNU1EQXlNREF3TWpBeE5qQXdNREUxT1RjPTwvWVdIPjxRU1pUPk1RPT08L1FTWlQ+PE5ZRE1KPk1qQXdMalU1PC9OWURNSj48R0RNSj5NekF3TGpBeDwvR0RNSj48TERNSj5OREF3TGpBeDwvTERNSj48Q0RNSj5OVEF3TGpBeDwvQ0RNSj48UVROWURNSj5OakF3TGpBeDwvUVROWURNSj48SlNZRE1KPk56QXdMakF4PC9KU1lETUo+PFdMWURNSj5PREF3TGpBeDwvV0xZRE1KPjxKRz5NVFF3TUE9PTwvSkc+PERKTFg+TVRBdzwvREpMWD48REpZWT42TCtaNUxpcTVwaXY1NW03Nks2dzVZNmY1WnVnPC9ESllZPjxESlNKPk1qQXhPUzB3TkMweE5TQXhORG93TXpvMU9BPT08L0RKU0o+PERCUj41NW03NTdDLzVMcTY8L0RCUj48WkRETT5SRTAxTlRnME9GVT08L1pERE0+PFFMUlhYTGlzdD48UUxSWFggbmFtZT0iNXAyRDVZaXA1THE2NUwraDVvR3YiPjxCRENEWUg+TVRNd01UQXlNREV5TURJelNrRXdNREF3TVZjd01EQXdNREF3TVE9PTwvQkRDRFlIPjxTWEg+TVE9PTwvU1hIPjxRTFJNQz41YnlnNUxpSjwvUUxSTUM+PEJEQ1FaSD5Xa2d4TWpNME5qVTNPRGs9PC9CRENRWkg+PFFaWVNYTEg+VTFreU1ERTVNRFl5TnpFeE1UYz08L1FaWVNYTEg+PFNGQ1pSPk1RPT08L1NGQ1pSPjxaSlpMPk1RPT08L1pKWkw+PFpKSD5Nekl3T1RnM01UazVPREE1TURrNE56WXk8L1pKSD48RlpKRz5lSGg0NVlXczVhNko1cHk2NVlXejwvRlpKRz48U1NIWT5NREl6TVE9PTwvU1NIWT48R0o+TVRReTwvR0o+PEhKU1pTUz5NVEV3TURBdzwvSEpTWlNTPjxYQj5NUT09PC9YQj48REg+TURFd0xUVTRORFExTlRVMjwvREg+PERaPjVZeVg1THFzNWJpQ2RYaDQ1WXk2NTRtYjZLR1g8L0RaPjxZQj5NVEV3TVRJejwvWUI+PEdaRFc+ZUhqbm1vVGxzSS9vZ1l6bGtaZz08L0daRFc+PERaWUo+TlRVNE5ESTFPRFUxT0RoQWNYRXVZMjl0PC9EWllKPjxRTFJMWD5NUT09PC9RTFJMWD48UUxCTD5Nakk9PC9RTEJMPjxHWUZTPk1BPT08L0dZRlM+PEdZUUs+NVlXeDVweUo1b09GNVlhMU1qTXlNdz09PC9HWVFLPjxCWj42TCtaNXBpdjVhU0g1ck9vTVRFPTwvQlo+PFlXSD5ORFk1TURBeU1EQXdNakF4TmpBd01ERTFPVGM9PC9ZV0g+PFFTWlQ+TUE9PTwvUVNaVD48QkRDTFg+TVE9PTwvQkRDTFg+PC9RTFJYWD48UUxSWFggbmFtZT0iNXAyRDVZaXA1THE2NUwraDVvR3YiPjxCRENEWUg+TVRNd01UQXlNREV5TURJelNrRXdNREF3TVZjd01EQXdNREF3TVE9PTwvQkRDRFlIPjxTWEg+TWc9PTwvU1hIPjxRTFJNQz41cDJPNVp1YjwvUUxSTUM+PEJEQ1FaSD5Xa2d4TWpNME5qVTNPRGs9PC9CRENRWkg+PFFaWVNYTEg+TWpJeU1qSXlNakl5TWpJeU1nPT08L1FaWVNYTEg+PFNGQ1pSPk1RPT08L1NGQ1pSPjxaSlpMPk1RPT08L1pKWkw+PFpKSD5Nekl3TVRBMU1UazVOREF5TVRnMU1UQXg8L1pKSD48RlpKRz5lSGg0NVlXczVhNko1cHk2NVlXek1nPT08L0ZaSkc+PFNTSFk+TURJek1RPT08L1NTSFk+PEdKPk1UUXk8L0dKPjxISlNaU1M+TVRFd01EQXc8L0hKU1pTUz48WEI+TVE9PTwvWEI+PERIPk1ERXdMVFU0TkRRMU5UVTI8L0RIPjxEWj41WXlYNUxxczViaUNkWGg0NVl5NjU0bWI2S0dYTWc9PTwvRFo+PFlCPk1URXdNVEl6PC9ZQj48R1pEVz5lSGpubW9UbHNJL29nWXpsa1pneTwvR1pEVz48RFpZSj5OVFU0TkRJMU9EVTFPRGhBY1hFdVkyOXQ8L0RaWUo+PFFMUkxYPk1RPT08L1FMUkxYPjxRTEJMPk1qST08L1FMQkw+PEdZRlM+TUE9PTwvR1lGUz48R1lRSz41WVd4NXB5SjVvT0Y1WWExTWpNeU13PT08L0dZUUs+PEJaPjZMK1o1cGl2NWFTSDVyT29Nakk9PC9CWj48WVdIPk5EWTVNREF5TURBd01qQXhOakF3TURFMU9UYz08L1lXSD48UVNaVD5NQT09PC9RU1pUPjxCRENMWD5NUT09PC9CRENMWD48L1FMUlhYPjwvUUxSWFhMaXN0PjwvVERTWVE+PC9URFNZUUxJU1Q+PEpTWURTWVFMSVNUPjxKU1lEU1lRIG5hbWU9IjVidTY2SzYrNTVTbzVaeXc1TDIvNTVTbzVwMkQ0NENCNWE2RjVaKzY1Wnl3NUwyLzU1U281cDJEIj48QkRDRFlIPk1UTXdNVEF5TURFek1EQTRSMEl3TURBd01sY3dNREF3TURBd01nPT08L0JEQ0RZSD48Wkw+UWVXNGdrTGxqTHJrdlpQb2dyTGxqSmZscEtmb29aY3hNT1dQdHc9PTwvWkw+PFlUPk1EZzA8L1lUPjxTWVFNSj5NVEl6TkM0MU5nPT08L1NZUU1KPjxTWVFRU1NKPk1qQXhPQzB3TVMwd01TQXhORG93TXpvMU9BPT08L1NZUVFTU0o+PFNZUUpTU0o+TWpBeE9TMHhNaTB4TWlBeE5Eb3dNem8xT0E9PTwvU1lRSlNTSj48UUxYWj5NVEF3PC9RTFhaPjxCRENRWkg+UTFGYVNERTFPRGMwTlRZNTwvQkRDUVpIPjxESkpHPjVyV0w2SytWZUhqbW5Mcm1ub1E9PC9ESkpHPjxZV0g+TkRZNU1EQXlNREF3TWpBeE5qQXdNREUxT1RBPTwvWVdIPjxRU1pUPk1RPT08L1FTWlQ+PFFESkc+TVRBd0xqSXc8L1FESkc+PERKTFg+TWpBdzwvREpMWD48REpZWT41NW03Nks2dzVZNmY1WnVnTVRJejwvREpZWT48REpTSj5NakF4T1Mwd05DMHhOU0F4TkRvd016bzFPQT09PC9ESlNKPjxEQlI+NTVtNzU3Qy81THE2TWpJPTwvREJSPjxaRERNPlJFMDROVFE0T0RoWTwvWkRETT48UUxSWFhMaXN0PjxRTFJYWCBuYW1lPSI1cDJENVlpcDVMcTY1TCtoNW9HdiI+PEJEQ0RZSD5NVE13TVRBeU1ERXpNREE0UjBJd01EQXdNbGN3TURBd01EQXdNZz09PC9CRENEWUg+PFNYSD5NUT09PC9TWEg+PFFMUk1DPjU2cW01YVc5NWE2SDwvUUxSTUM+PEJEQ1FaSD5RMUZhU0RFMU9EYzBOVFk1PC9CRENRWkg+PFFaWVNYTEg+TXpNek16TXpNek16TXpNPTwvUVpZU1hMSD48U0ZDWlI+TVE9PTwvU0ZDWlI+PFpKWkw+TVE9PTwvWkpaTD48WkpIPk16SXdNVEExTVRrNU5EQTNNVEl4T1RVNTwvWkpIPjxGWkpHPmVIaDQ1WVdzNWE2SjVweTY1WVd6PC9GWkpHPjxTU0hZPk1ESXpNUT09PC9TU0hZPjxHSj5NVFF5PC9HSj48SEpTWlNTPk1URXdNREF3PC9ISlNaU1M+PFhCPk1RPT08L1hCPjxESD5NREV3TFRVNE5EUTFOVFUyPC9ESD48RFo+NVl5WDVMcXM1YmlDZFhoNDVZeTY1NG1iNktHWDwvRFo+PFlCPk1URXdNVEl6PC9ZQj48R1pEVz5lSGpubW9UbHNJL29nWXpsa1pnPTwvR1pEVz48RFpZSj5OVFU0TkRJMU9EVTFPRGhBY1hFdVkyOXQ8L0RaWUo+PFFMUkxYPk1RPT08L1FMUkxYPjxRTEJMPk1qST08L1FMQkw+PEdZRlM+TUE9PTwvR1lGUz48R1lRSz41WVd4NXB5SjVvT0Y1WWExTWpNeU13PT08L0dZUUs+PEJaPjZMK1o1cGl2NWFTSDVyT29NVEU9PC9CWj48WVdIPk5EWTVNREF5TURBd01qQXhOakF3TURFMU9UQT08L1lXSD48UVNaVD5NQT09PC9RU1pUPjxCRENMWD5NUT09PC9CRENMWD48L1FMUlhYPjxRTFJYWCBuYW1lPSI1cDJENVlpcDVMcTY1TCtoNW9HdiI+PEJEQ0RZSD5NVE13TVRBeU1ERXpNREE0UjBJd01EQXdNbGN3TURBd01EQXdNZz09PC9CRENEWUg+PFNYSD5NZz09PC9TWEg+PFFMUk1DPjVicUU1WTJhNloyejwvUUxSTUM+PEJEQ1FaSD5RMUZhU0RFMU9EYzBOVFk1PC9CRENRWkg+PFFaWVNYTEg+TkRRME5EUTBORFEwPC9RWllTWExIPjxTRkNaUj5NUT09PC9TRkNaUj48WkpaTD5NUT09PC9aSlpMPjxaSkg+TXpJd01UQTFNVGszTmpBME1EUTVOVFUxPC9aSkg+PEZaSkc+ZUhoNDVZV3M1YTZKNXB5NjVZV3o8L0ZaSkc+PFNTSFk+TURJek1RPT08L1NTSFk+PEdKPk1UUXk8L0dKPjxISlNaU1M+TVRFd01EQXc8L0hKU1pTUz48WEI+TVE9PTwvWEI+PERIPk1ERXdMVFU0TkRRMU5UVTI8L0RIPjxEWj41WXlYNUxxczViaUNkWGg0NVl5NjU0bWI2S0dYPC9EWj48WUI+TVRFd01USXo8L1lCPjxHWkRXPmVIam5tb1Rsc0kvb2dZemxrWmc9PC9HWkRXPjxEWllKPk5UVTROREkxT0RVMU9EaEFjWEV1WTI5dDwvRFpZSj48UUxSTFg+TVE9PTwvUUxSTFg+PFFMQkw+TWpJPTwvUUxCTD48R1lGUz5NQT09PC9HWUZTPjxHWVFLPjVZV3g1cHlKNW9PRjVZYTFNak15TXc9PTwvR1lRSz48Qlo+NkwrWjVwaXY1YVNINXJPb01URT08L0JaPjxZV0g+TkRZNU1EQXlNREF3TWpBeE5qQXdNREUxT1RBPTwvWVdIPjxRU1pUPk1BPT08L1FTWlQ+PEJEQ0xYPk1RPT08L0JEQ0xYPjwvUUxSWFg+PC9RTFJYWExpc3Q+PC9KU1lEU1lRPjwvSlNZRFNZUUxJU1Q+PEZEQ1FMSVNUPjxGRENRIG5hbWU9IjVvaS81Wnl3NUxxbjVwMkQiPjxCRENEWUg+TVRNd01UQTFNREEyTURBeFIwSXdNREF3TWtZd01EQXhNREF3TVE9PTwvQkRDRFlIPjxGRFpMPlFlVzRna0xsakxwRDViQ1A1WXk2UlRZdE15MHlNREk9PC9GRFpMPjxKWk1KPk5UQXVOalE9PC9KWk1KPjxaWUpaTUo+TlRBdU1EQT08L1pZSlpNSj48RlRKWk1KPk1UQXVOalE9PC9GVEpaTUo+PEdIWVQ+TVRFeDwvR0hZVD48RldYWj5Ndz09PC9GV1haPjxKR1NKPk1qQXhNUzB3TWkweE1pQXhORG93TXpvMU9BPT08L0pHU0o+PFREU1lRU1NKPk1qQXhPQzB3TVMwd01TQXdNVG93TVRvMU9BPT08L1REU1lRU1NKPjxURFNZSlNTSj5NakF4T1MweE1TMHhNU0F4TVRveE1UbzFPQT09PC9URFNZSlNTSj48QkRDUVpIPlExRmFTREF5T1RJNU16Z3hPRGt5PC9CRENRWkg+PERKSkc+ZUhoNDU1bTc2SzZ3NXB5NjVwNkU8L0RKSkc+PFlXSD5ORFk1TURBeU1EQXdNakF4TmpBd01ERTFPVEU9PC9ZV0g+PFFTWlQ+TVE9PTwvUVNaVD48RkRDSllKRz5NVEF5TWpBd0xqVTM8L0ZEQ0pZSkc+PFREU1lRUj41WnlmNVp5dzVMMi81NVNvNXAyRDVMcTY8L1REU1lRUj48REpMWD5NakF3PC9ESkxYPjxESllZPjU1bTc2SzZ3NVk2ZjVadWdNek09PC9ESllZPjxESlNKPk1qQXhPUzB3TkMweE1TQXhORG93TXpvMU9BPT08L0RKU0o+PERCUj41NW03NTdDLzVMcTZNek09PC9EQlI+PFpERE0+UkUwd01EQXo8L1pERE0+PFFMUlhYTGlzdD48UUxSWFggbmFtZT0iNXAyRDVZaXA1THE2NUwraDVvR3YiPjxCRENEWUg+TVRNd01UQTFNREEyTURBeFIwSXdNREF3TWtZd01EQXhNREF3TVE9PTwvQkRDRFlIPjxTWEg+TVE9PTwvU1hIPjxRTFJNQz41cCt6NW95djVadTk8L1FMUk1DPjxCRENRWkg+UTFGYVNEQXlPVEk1TXpneE9Ea3k8L0JEQ1FaSD48UVpZU1hMSD5OVFUxTlRVMU5UVTFOVFU9PC9RWllTWExIPjxTRkNaUj5NUT09PC9TRkNaUj48WkpaTD5NUT09PC9aSlpMPjxaSkg+TXpJd01UQTFNVGs0T0RBME1qVXpOemt3PC9aSkg+PEZaSkc+ZUhoNDVZV3M1YTZKNXB5NjVZV3o8L0ZaSkc+PFNTSFk+TURJek1RPT08L1NTSFk+PEdKPk1UUXk8L0dKPjxISlNaU1M+TVRFd01EQXc8L0hKU1pTUz48WEI+TVE9PTwvWEI+PERIPk1ERXdMVFU0TkRRMU5UVTI8L0RIPjxEWj41WXlYNUxxczViaUNkWGg0NVl5NjU0bWI2S0dYPC9EWj48WUI+TVRFd01USXo8L1lCPjxHWkRXPmVIam5tb1Rsc0kvb2dZemxrWmc9PC9HWkRXPjxEWllKPk5UVTROREkxT0RVMU9EaEFjWEV1WTI5dDwvRFpZSj48UUxSTFg+TVE9PTwvUUxSTFg+PFFMQkw+TWpJPTwvUUxCTD48R1lGUz5NQT09PC9HWUZTPjxHWVFLPjVZV3g1cHlKNW9PRjVZYTFNak15TXc9PTwvR1lRSz48Qlo+NkwrWjVwaXY1YVNINXJPb01URT08L0JaPjxZV0g+TkRZNU1EQXlNREF3TWpBeE5qQXdNREUxT1RFPTwvWVdIPjxRU1pUPk1BPT08L1FTWlQ+PEJEQ0xYPk1RPT08L0JEQ0xYPjwvUUxSWFg+PFFMUlhYIG5hbWU9IjVwMkQ1WWlwNUxxNjVMK2g1b0d2Ij48QkRDRFlIPk1UTXdNVEExTURBMk1EQXhSMEl3TURBd01rWXdNREF4TURBd01RPT08L0JEQ0RZSD48U1hIPk1nPT08L1NYSD48UUxSTUM+NWJ5ZzU0RzE1NmVMPC9RTFJNQz48QkRDUVpIPlExRmFTREF5T1RJNU16Z3hPRGt5PC9CRENRWkg+PFFaWVNYTEg+TmpZMk5qWTJOalkyPC9RWllTWExIPjxTRkNaUj5NUT09PC9TRkNaUj48WkpaTD5NUT09PC9aSlpMPjxaSkg+TXpJd01UQTFNVGs0TlRFd01qVTBNVEl5PC9aSkg+PEZaSkc+ZUhoNDVZV3M1YTZKNXB5NjVZV3o8L0ZaSkc+PFNTSFk+TURJek1RPT08L1NTSFk+PEdKPk1UUXk8L0dKPjxISlNaU1M+TVRFd01EQXc8L0hKU1pTUz48WEI+TWc9PTwvWEI+PERIPk1ERXdMVFU0TkRRMU5UVTI8L0RIPjxEWj41WXlYNUxxczViaUNkWGg0NVl5NjU0bWI2S0dYPC9EWj48WUI+TVRFd01USXo8L1lCPjxHWkRXPmVIam5tb1Rsc0kvb2dZemxrWmc9PC9HWkRXPjxEWllKPk5UVTROREkxT0RVMU9EaEFjWEV1WTI5dDwvRFpZSj48UUxSTFg+TVE9PTwvUUxSTFg+PFFMQkw+TWpJPTwvUUxCTD48R1lGUz5NQT09PC9HWUZTPjxHWVFLPjVZV3g1cHlKNW9PRjVZYTFNak15TXc9PTwvR1lRSz48Qlo+NkwrWjVwaXY1YVNINXJPb01URT08L0JaPjxZV0g+TkRZNU1EQXlNREF3TWpBeE5qQXdNREUxT1RFPTwvWVdIPjxRU1pUPk1BPT08L1FTWlQ+PEJEQ0xYPk1RPT08L0JEQ0xYPjwvUUxSWFg+PC9RTFJYWExpc3Q+PC9GRENRPjwvRkRDUUxJU1Q+PEhZU1lRTElTVD48SFlTWVEgbmFtZT0iNXJXMzVaK2ZLT1dRcSthWG9PV3hoZWF3a2VhMXQrV3lteW5rdmIvbmxLam1uWU09Ij48QkRDRFlIPk9URXdOVEEwTVRBMU1qQXpSMGd3TURBeU5FZ3dNREF4TURBd01RPT08L0JEQ0RZSD48WE1NQz41cCtRNTVTbzVyVzM2YUc1NTV1dTwvWE1NQz48WUhXWlNNPjVwK1E1cCtRNXJXMzVaK2Y8L1lIV1pTTT48WUhMWEE+TWc9PTwvWUhMWEE+PFlITFhCPk1qUT08L1lITFhCPjxIRE1DPjZZQ042WUdsNWJLYjwvSERNQz48SERXWj41TGl0NVp1OTVZMlg1clczPC9IRFdaPjxIRFlUPk1RPT08L0hEWVQ+PFNZUU1KPk9UQXdMakF3TURBPTwvU1lRTUo+PFNZUVFTU0o+TWpBeE9DMHdNaTB4TWlBeE1qb3dNem8xT0E9PTwvU1lRUVNTSj48U1lRSlNTSj5NakF4T1MweE1pMHhNaUF4TWpvd016bzFPQT09PC9TWVFKU1NKPjxCRENRWkg+UTFGYVNERXdNREF3TkE9PTwvQkRDUVpIPjxESkpHPmVIaDQ1NXFFNTVtNzZLNnc1cHk2NXA2RTwvREpKRz48WVdIPk5EWTVNREF5TURBd01qQXhOakF3TURFMU9UST08L1lXSD48UVNaVD5NUT09PC9RU1pUPjxTWUpaRT5NakF3TURBdU9Uaz08L1NZSlpFPjxTWUpCWllKPjVxQ0g1WWVHNUw2ZDVvMnVNUT09PC9TWUpCWllKPjxTWUpKTlFLPjVxMmo1Ymk0NTd5MDU3cXo8L1NZSkpOUUs+PERKTFg+TWpBdzwvREpMWD48REpZWT41NW03Nks2dzVZNmY1WnVnPC9ESllZPjxESlNKPk1qQXhPUzB3TkMweE5TQXhORG93TXpvMU9BPT08L0RKU0o+PERCUj41NW03NTdDLzVMcTY8L0RCUj48WkhETT5SRTB3TURBejwvWkhETT48UUxSWFhMaXN0PjxRTFJYWCBuYW1lPSI1cDJENVlpcDVMcTY1TCtoNW9HdiI+PEJEQ0RZSD5PVEV3TlRBME1UQTFNakF6UjBnd01EQXlORWd3TURBeE1EQXdNUT09PC9CRENEWUg+PFNYSD5NUT09PC9TWEg+PFFMUk1DPjVZdSs1cldwNlp1bzwvUUxSTUM+PEJEQ1FaSD5RMUZhU0RFd01EQXdOQT09PC9CRENRWkg+PFFaWVNYTEg+TnpjM056YzNOdz09PC9RWllTWExIPjxTRkNaUj5NUT09PC9TRkNaUj48WkpaTD5NUT09PC9aSlpMPjxaSkg+TXpJd01UQTFNVGszTlRBNU1qRTROemM1PC9aSkg+PEZaSkc+ZUhoNDVZV3M1YTZKNXB5NjVZV3o8L0ZaSkc+PFNTSFk+TURJek1RPT08L1NTSFk+PEdKPk1UUXk8L0dKPjxISlNaU1M+TVRFd01EQXc8L0hKU1pTUz48WEI+TVE9PTwvWEI+PERIPk1ERXdMVFU0TkRRMU5UVTI8L0RIPjxEWj41WXlYNUxxczViaUNkWGg0NVl5NjU0bWI2S0dYPC9EWj48WUI+TVRFd01USXo8L1lCPjxHWkRXPmVIam5tb1Rsc0kvb2dZemxrWmc9PC9HWkRXPjxEWllKPk5UVTROREkxT0RVMU9EaEFjWEV1WTI5dDwvRFpZSj48UUxSTFg+TVE9PTwvUUxSTFg+PFFMQkw+TWpJPTwvUUxCTD48R1lGUz5NQT09PC9HWUZTPjxHWVFLPjVZV3g1cHlKNW9PRjVZYTFNak15TXc9PTwvR1lRSz48Qlo+NkwrWjVwaXY1YVNINXJPb01URT08L0JaPjxZV0g+TkRZNU1EQXlNREF3TWpBeE5qQXdNREUxT1RJPTwvWVdIPjxRU1pUPk1BPT08L1FTWlQ+PEJEQ0xYPk1RPT08L0JEQ0xYPjwvUUxSWFg+PFFMUlhYIG5hbWU9IjVwMkQ1WWlwNUxxNjVMK2g1b0d2Ij48QkRDRFlIPk9URXdOVEEwTVRBMU1qQXpSMGd3TURBeU5FZ3dNREF4TURBd01RPT08L0JEQ0RZSD48U1hIPk1nPT08L1NYSD48UUxSTUM+NmFHKzVvR1M1cldwPC9RTFJNQz48QkRDUVpIPlExRmFTREV3TURBd05BPT08L0JEQ1FaSD48UVpZU1hMSD5PRGc0T0RnNE9EZz08L1FaWVNYTEg+PFNGQ1pSPk1RPT08L1NGQ1pSPjxaSlpMPk1RPT08L1pKWkw+PFpKSD5Nekl3TVRBMU1UazVNREE1TVRVd05URTU8L1pKSD48RlpKRz5lSGg0NVlXczVhNko1cHk2NVlXejwvRlpKRz48U1NIWT5NREl6TVE9PTwvU1NIWT48R0o+TVRReTwvR0o+PEhKU1pTUz5NVEV3TURBdzwvSEpTWlNTPjxYQj5NUT09PC9YQj48REg+TURFd0xUVTRORFExTlRVMjwvREg+PERaPjVZeVg1THFzNWJpQ2RYaDQ1WXk2NTRtYjZLR1g8L0RaPjxZQj5NVEV3TVRJejwvWUI+PEdaRFc+ZUhqbm1vVGxzSS9vZ1l6bGtaZz08L0daRFc+PERaWUo+TlRVNE5ESTFPRFUxT0RoQWNYRXVZMjl0PC9EWllKPjxRTFJMWD5NUT09PC9RTFJMWD48UUxCTD5Nakk9PC9RTEJMPjxHWUZTPk1BPT08L0dZRlM+PEdZUUs+NVlXeDVweUo1b09GNVlhMU1qTXlNdz09PC9HWVFLPjxCWj42TCtaNXBpdjVhU0g1ck9vTVRFPTwvQlo+PFlXSD5ORFk1TURBeU1EQXdNakF4TmpBd01ERTFPVEk9PC9ZV0g+PFFTWlQ+TUE9PTwvUVNaVD48QkRDTFg+TVE9PTwvQkRDTFg+PC9RTFJYWD48L1FMUlhYTGlzdD48L0hZU1lRPjwvSFlTWVFMSVNUPjxHSlpXU1lRTElTVD48R0paV1NZUSBuYW1lPSI1cDZFNzd5STVidTY3N3lKNTYyUjU0bXA1b21BNXB5SjVwMkQiPjxCRENEWUg+TlRFd05UQTBNVEExTWpBelIwSXdNREF5TkZRd01EQXhNREF3TVE9PTwvQkRDRFlIPjxaTD41cnVvNXJtVzVZeTY1THFSNkxDMzZMZXY1THVsNVkyWDwvWkw+PEdKWldHSFlUPk1URXg8L0dKWldHSFlUPjxHSlpXTUo+TVRBd0xqQXc8L0dKWldNSj48VERIWVNZUVNTSj5NakF4T0Mwd01pMHhNaUF4TWpvd016bzFPQT09PC9UREhZU1lRU1NKPjxUREhZU1lKU1NKPk1qQXhPUzB4TUMweE1pQXdNVG93TXpvMU9BPT08L1RESFlTWUpTU0o+PEJEQ1FaSD5RMUZhU0RFd01EQXdOUT09PC9CRENRWkg+PERKSkc+ZUhoNDU1cUU1NW03Nks2dzVweTY1cDZFPC9ESkpHPjxZV0g+TkRZNU1EQXlNREF3TWpBeE5qQXdNREUxT1RNPTwvWVdIPjxRU1pUPk1RPT08L1FTWlQ+PFRESFlTWVFSPjVMMi81NVNvNUxxNk1URXg8L1RESFlTWVFSPjxUREhZU1lNSj5OREF3TGpnNDwvVERIWVNZTUo+PEdKWldMWD5NZz09PC9HSlpXTFg+PEpHU0o+TWpBeE9TMHdOQzB5TlNBeE5Eb3dNem8xT0E9PTwvSkdTSj48REpTSj5NakF4T0Mwd05DMHhOU0F4TkRvd016bzFPQT09PC9ESlNKPjxEQlI+NTVtNzU3Qy81THE2PC9EQlI+PFFMUlhYTGlzdD48UUxSWFggbmFtZT0iNXAyRDVZaXA1THE2NUwraDVvR3YiPjxCRENEWUg+TlRFd05UQTBNVEExTWpBelIwSXdNREF5TkZRd01EQXhNREF3TVE9PTwvQkRDRFlIPjxTWEg+TVE9PTwvU1hIPjxRTFJNQz41YTJVNXJhYjZJMmo8L1FMUk1DPjxCRENRWkg+UTFGYVNERXdNREF3TlE9PTwvQkRDUVpIPjxRWllTWExIPk9UazVPVGs1T1RrNTwvUVpZU1hMSD48U0ZDWlI+TVE9PTwvU0ZDWlI+PFpKWkw+TVE9PTwvWkpaTD48WkpIPk16SXdNVEExTVRrNU16QTNNVFkxTmpVMTwvWkpIPjxGWkpHPmVIaDQ1WVdzNWE2SjVweTY1WVd6PC9GWkpHPjxTU0hZPk1ESXpNUT09PC9TU0hZPjxHSj5NVFF5PC9HSj48SEpTWlNTPk1URXdNREF3PC9ISlNaU1M+PFhCPk1RPT08L1hCPjxESD5NREV3TFRVNE5EUTFOVFUyPC9ESD48RFo+NVl5WDVMcXM1YmlDZFhoNDVZeTY1NG1iNktHWDwvRFo+PFlCPk1URXdNVEl6PC9ZQj48R1pEVz5lSGpubW9UbHNJL29nWXpsa1pnPTwvR1pEVz48RFpZSj5OVFU0TkRJMU9EVTFPRGhBY1hFdVkyOXQ8L0RaWUo+PFFMUkxYPk1RPT08L1FMUkxYPjxRTEJMPk1qST08L1FMQkw+PEdZRlM+TUE9PTwvR1lGUz48R1lRSz41WVd4NXB5SjVvT0Y1WWExTWpNeU13PT08L0dZUUs+PEJaPjZMK1o1cGl2NWFTSDVyT29NVEU9PC9CWj48WVdIPk5EWTVNREF5TURBd01qQXhOakF3TURFMU9UTT08L1lXSD48UVNaVD5NQT09PC9RU1pUPjxCRENMWD5NUT09PC9CRENMWD48L1FMUlhYPjxRTFJYWCBuYW1lPSI1cDJENVlpcDVMcTY1TCtoNW9HdiI+PEJEQ0RZSD5OVEV3TlRBME1UQTFNakF6UjBJd01EQXlORlF3TURBeE1EQXdNUT09PC9CRENEWUg+PFNYSD5NZz09PC9TWEg+PFFMUk1DPjZZS2k2SWlTPC9RTFJNQz48QkRDUVpIPlExRmFTREV3TURBd05RPT08L0JEQ1FaSD48UVpZU1hMSD5NREE1TURrd09UQTVNRGt3PC9RWllTWExIPjxTRkNaUj5NUT09PC9TRkNaUj48WkpaTD5NUT09PC9aSlpMPjxaSkg+TXpJd01UQTFNVGszT0RBMU1qQXpOelU0PC9aSkg+PEZaSkc+ZUhoNDVZV3M1YTZKNXB5NjVZV3o8L0ZaSkc+PFNTSFk+TURJek1RPT08L1NTSFk+PEdKPk1UUXk8L0dKPjxISlNaU1M+TVRFd01EQXc8L0hKU1pTUz48WEI+TVE9PTwvWEI+PERIPk1ERXdMVFU0TkRRMU5UVTI8L0RIPjxEWj41WXlYNUxxczViaUNkWGg0NVl5NjU0bWI2S0dYPC9EWj48WUI+TVRFd01USXo8L1lCPjxHWkRXPmVIam5tb1Rsc0kvb2dZemxrWmc9PC9HWkRXPjxEWllKPk5UVTROREkxT0RVMU9EaEFjWEV1WTI5dDwvRFpZSj48UUxSTFg+TVE9PTwvUUxSTFg+PFFMQkw+TWpJPTwvUUxCTD48R1lGUz5NQT09PC9HWUZTPjxHWVFLPjVZV3g1cHlKNW9PRjVZYTFNak15TXc9PTwvR1lRSz48Qlo+NkwrWjVwaXY1YVNINXJPb01URT08L0JaPjxZV0g+TkRZNU1EQXlNREF3TWpBeE5qQXdNREUxT1RNPTwvWVdIPjxRU1pUPk1BPT08L1FTWlQ+PEJEQ0xYPk1RPT08L0JEQ0xYPjwvUUxSWFg+PC9RTFJYWExpc3Q+PC9HSlpXU1lRPjwvR0paV1NZUUxJU1Q+PExRTElTVD48TFEgbmFtZT0iNXA2WDVwMkQiPjxCRENEWUg+TlRFd05UQTBNVEExTWpBelIwSXdNREF5TkZRd01EQXhNREF3TWc9PTwvQkRDRFlIPjxaTD41N3VFNVpPZjU3MlhNVEl6PC9aTD48U1lRTUo+TVRVd05qSXVNREF3TUE9PTwvU1lRTUo+PExEU1lRU1NKPk1qQXhPQzB3TWkweE1pQXhNam93TXpvMU9BPT08L0xEU1lRU1NKPjxMRFNZSlNTSj5NakF4T1Mwd05pMHhNaUF4TkRvd016bzFPQT09PC9MRFNZSlNTSj48TERTWVFYWj5NUT09PC9MRFNZUVhaPjxCRENRWkg+UTFGYVNERXdNREF3Tmc9PTwvQkRDUVpIPjxESkpHPmVIaDQ1NXFFNTVtNzZLNnc1cHk2NXA2RTwvREpKRz48WVdIPk5EWTVNREF5TURBd01qQXhOakF3TURFMU9UUT08L1lXSD48UVNaVD5NUT09PC9RU1pUPjxGQkY+NVkrUjVZeUY1cGE1NXBpdjZMQ0I8L0ZCRj48U0xMTVNZUVIxPjVvbUE1cHlKNXAyRDVMcTZNUT09PC9TTExNU1lRUjE+PFNMTE1TWVFSMj41b21BNXB5SjVwMkQ1THE2TWc9PTwvU0xMTVNZUVIyPjxaWVNaPjZJdTU1cDZjNXFDUjwvWllTWj48WlM+TVRVNE1nPT08L1pTPjxMWj5NVFV5PC9MWj48UVk+NkxXMzVycVE8L1FZPjxaTE5EPk5BPT08L1pMTkQ+PExCPlRFSXdNUT09PC9MQj48WEI+V0VJd01EQXg8L1hCPjxYRE0+NWJDUDVaeXc1WkNOTWpJeTwvWERNPjxESllZPjU1bTc2SzZ3NVk2ZjVadWdOVFU9PC9ESllZPjxESlNKPk1qQXhPUzB3TkMwME5TQXhORG93TXpvMU9BPT08L0RKU0o+PERCUj41NW03NTdDLzVMcTY8L0RCUj48REpMWD5NakF3PC9ESkxYPjxRTFJYWExpc3Q+PFFMUlhYIG5hbWU9IjVwMkQ1WWlwNUxxNjVMK2g1b0d2Ij48QkRDRFlIPk5URXdOVEEwTVRBMU1qQXpSMEl3TURBeU5GUXdNREF4TURBd01nPT08L0JEQ0RZSD48U1hIPk1RPT08L1NYSD48UUxSTUM+NmIyUTVwbUw2Ym1QPC9RTFJNQz48QkRDUVpIPlExRmFTREV3TURBd05nPT08L0JEQ1FaSD48UVpZU1hMSD5NRGt3T1RBeU1UTXhNak09PC9RWllTWExIPjxTRkNaUj5NUT09PC9TRkNaUj48WkpaTD5NUT09PC9aSlpMPjxaSkg+TkRFeE56SXlNVGszTlRBM01UVTFOelV6PC9aSkg+PEZaSkc+ZUhoNDVZV3M1YTZKNXB5NjVZV3o8L0ZaSkc+PFNTSFk+TURJek1RPT08L1NTSFk+PEdKPk1UUXk8L0dKPjxISlNaU1M+TVRFd01EQXc8L0hKU1pTUz48WEI+TVE9PTwvWEI+PERIPk1ERXdMVFU0TkRRMU5UVTI8L0RIPjxEWj41WXlYNUxxczViaUNkWGg0NVl5NjU0bWI2S0dYPC9EWj48WUI+TVRFd01USXo8L1lCPjxHWkRXPmVIam5tb1Rsc0kvb2dZemxrWmc9PC9HWkRXPjxEWllKPk5UVTROREkxT0RVMU9EaEFjWEV1WTI5dDwvRFpZSj48UUxSTFg+TVE9PTwvUUxSTFg+PFFMQkw+TWpJPTwvUUxCTD48R1lGUz5NQT09PC9HWUZTPjxHWVFLPjVZV3g1cHlKNW9PRjVZYTFNak15TXc9PTwvR1lRSz48Qlo+NkwrWjVwaXY1YVNINXJPb01URT08L0JaPjxZV0g+TkRZNU1EQXlNREF3TWpBeE5qQXdNREUxT1RRPTwvWVdIPjxRU1pUPk1BPT08L1FTWlQ+PEJEQ0xYPk1RPT08L0JEQ0xYPjwvUUxSWFg+PFFMUlhYIG5hbWU9IjVwMkQ1WWlwNUxxNjVMK2g1b0d2Ij48QkRDRFlIPk5URXdOVEEwTVRBMU1qQXpSMEl3TURBeU5GUXdNREF4TURBd01nPT08L0JEQ0RZSD48U1hIPk1nPT08L1NYSD48UUxSTUM+NXBlMjZibVA1NFdLPC9RTFJNQz48QkRDUVpIPlExRmFTREV3TURBd05nPT08L0JEQ1FaSD48UVpZU1hMSD5NVEl4TWpFeU1USXhNakV5TVRJPTwvUVpZU1hMSD48U0ZDWlI+TVE9PTwvU0ZDWlI+PFpKWkw+TVE9PTwvWkpaTD48WkpIPk5ERXhOekl5TVRrM09UQTJNalV5TlRNMDwvWkpIPjxGWkpHPmVIaDQ1WVdzNWE2SjVweTY1WVd6PC9GWkpHPjxTU0hZPk1ESXpNUT09PC9TU0hZPjxHSj5NVFF5PC9HSj48SEpTWlNTPk1URXdNREF3PC9ISlNaU1M+PFhCPk1RPT08L1hCPjxESD5NREV3TFRVNE5EUTFOVFUyPC9ESD48RFo+NVl5WDVMcXM1YmlDZFhoNDVZeTY1NG1iNktHWDwvRFo+PFlCPk1URXdNVEl6PC9ZQj48R1pEVz5lSGpubW9UbHNJL29nWXpsa1pnPTwvR1pEVz48RFpZSj5OVFU0TkRJMU9EVTFPRGhBY1hFdVkyOXQ8L0RaWUo+PFFMUkxYPk1RPT08L1FMUkxYPjxRTEJMPk1qST08L1FMQkw+PEdZRlM+TUE9PTwvR1lGUz48R1lRSz41WVd4NXB5SjVvT0Y1WWExTWpNeU13PT08L0dZUUs+PEJaPjZMK1o1cGl2NWFTSDVyT29NVEU9PC9CWj48WVdIPk5EWTVNREF5TURBd01qQXhOakF3TURFMU9UUT08L1lXSD48UVNaVD5NQT09PC9RU1pUPjxCRENMWD5NUT09PC9CRENMWD48L1FMUlhYPjwvUUxSWFhMaXN0PjwvTFE+PC9MUUxJU1Q+PERZQVFMSVNUPjxEWUFRIG5hbWU9IjVvcTE1b3E4NXAyRCI+PEJEQ0RZSD5NVE13TVRBMU1EQTJNREF4UjBJd01EQXdNa1l3TURBeE1EQXlNUT09PC9CRENEWUg+PERZQkRDTFg+TWc9PTwvRFlCRENMWD48Wkw+UWVXNGdrTGxqTHBENWJDUDVZeTZSVFl0TXkweU1EST08L1pMPjxEWVI+NWJ5ZzVMaUo8L0RZUj48RFlGUz5NUT09PC9EWUZTPjxCREJaWlFTRT5NVEl6TVRBd0xqRXlNelE9PC9CREJaWlFTRT48WldMWFFTU0o+TWpBeE9DMHdOQzB4TlNBeE5Eb3dNem8xT0E9PTwvWldMWFFTU0o+PFpXTFhKU1NKPk1qQXhPUzB3TkMweE5TQXhORG93TXpvMU9BPT08L1pXTFhKU1NKPjxCRENESlpNSD5XazFJTURBd01USXo8L0JEQ0RKWk1IPjxESkpHPmVIaDQ1NXFFNTVtNzZLNnc1cHk2NXA2RTwvREpKRz48WVdIPk5EWTVNREF5TURBd01qQXhOakF3TURFMU9UVT08L1lXSD48UVNaVD5NUT09PC9RU1pUPjxaSkpaV1pMPjVaMlE2SkM5NVp5b2VIamxqTHA0ZU9pM3IzaDQ1YkNQNVl5NjwvWkpKWldaTD48WkpKWldEWUZXPk5UWTFOZz09PC9aSkpaV0RZRlc+PFpHWlFRRFNTPjVweUE2YXVZNVlDNjVwMkQ1Nkd1NWE2YTVMcUw1YTZlTWpNPTwvWkdaUVFEU1M+PFpHWlFTRT5NelF6TWpRdU1URT08L1pHWlFTRT48WlhEWVlXSD5NVFF6TXpReU16SXpNdz09PC9aWERZWVdIPjxaWERZWVk+TWpBeE9TMHdOQzB4TlNBeE5Eb3dNem8xT0E9PTwvWlhEWVlZPjxaWFNKPk1qQXhPUzB3TkMweU5TQXhORG93TXpvMU9BPT08L1pYU0o+PERKTFg+TWpBdzwvREpMWD48REpZWT41NW03Nks2dzVZNmY1WnVnPC9ESllZPjxESlNKPk1qQXhPUzB3TkMwME5TQXhORG93TXpvMU9BPT08L0RKU0o+PERCUj41NW03NTdDLzVMcTY8L0RCUj48UUxSWFhMaXN0PjxRTFJYWCBuYW1lPSI1cDJENVlpcDVMcTY1TCtoNW9HdiI+PEJEQ0RZSD5NVE13TVRBMU1EQTJNREF4UjBJd01EQXdNa1l3TURBeE1EQXlNUT09PC9CRENEWUg+PFNYSD5NUT09PC9TWEg+PFFMUk1DPjZZZVI1ck85NXJTTDwvUUxSTUM+PEJEQ1FaSD5XazFJTURBd01USXo8L0JEQ1FaSD48UVpZU1hMSD5NVE14TXpFek1UTXhNekV6TVRNPTwvUVpZU1hMSD48U0ZDWlI+TVE9PTwvU0ZDWlI+PFpKWkw+TVE9PTwvWkpaTD48WkpIPk5ERXhOekl5TVRrM05qQXlNalU1TlRFNDwvWkpIPjxGWkpHPmVIaDQ1WVdzNWE2SjVweTY1WVd6PC9GWkpHPjxTU0hZPk1ESXpNUT09PC9TU0hZPjxHSj5NVFF5PC9HSj48SEpTWlNTPk1URXdNREF3PC9ISlNaU1M+PFhCPk1RPT08L1hCPjxESD5NREV3TFRVNE5EUTFOVFUyPC9ESD48RFo+NVl5WDVMcXM1YmlDZFhoNDVZeTY1NG1iNktHWDwvRFo+PFlCPk1URXdNVEl6PC9ZQj48R1pEVz5lSGpubW9UbHNJL29nWXpsa1pnPTwvR1pEVz48RFpZSj5OVFU0TkRJMU9EVTFPRGhBY1hFdVkyOXQ8L0RaWUo+PFFMUkxYPk1RPT08L1FMUkxYPjxRTEJMPk1qST08L1FMQkw+PEdZRlM+TUE9PTwvR1lGUz48R1lRSz41WVd4NXB5SjVvT0Y1WWExTWpNeU13PT08L0dZUUs+PEJaPjZMK1o1cGl2NWFTSDVyT29NVEU9PC9CWj48WVdIPk5EWTVNREF5TURBd01qQXhOakF3TURFMU9UVT08L1lXSD48UVNaVD5NQT09PC9RU1pUPjxCRENMWD5NUT09PC9CRENMWD48L1FMUlhYPjxRTFJYWCBuYW1lPSI1cDJENVlpcDVMcTY1TCtoNW9HdiI+PEJEQ0RZSD5NVE13TVRBMU1EQTJNREF4UjBJd01EQXdNa1l3TURBeE1EQXlNUT09PC9CRENEWUg+PFNYSD5NZz09PC9TWEg+PFFMUk1DPjVwK1A1YjJtNVkyYTwvUUxSTUM+PEJEQ1FaSD5XazFJTURBd01USXo8L0JEQ1FaSD48UVpZU1hMSD5NVFF4TkRFME1UUXhOREUwTVRReE5ERTA8L1FaWVNYTEg+PFNGQ1pSPk1RPT08L1NGQ1pSPjxaSlpMPk1RPT08L1pKWkw+PFpKSD5OREV4TnpJeU1UazROREEwTWpVNE5qYzA8L1pKSD48RlpKRz5lSGg0NVlXczVhNko1cHk2NVlXejwvRlpKRz48U1NIWT5NREl6TVE9PTwvU1NIWT48R0o+TVRReTwvR0o+PEhKU1pTUz5NVEV3TURBdzwvSEpTWlNTPjxYQj5NUT09PC9YQj48REg+TURFd0xUVTRORFExTlRVMjwvREg+PERaPjVZeVg1THFzNWJpQ2RYaDQ1WXk2NTRtYjZLR1g8L0RaPjxZQj5NVEV3TVRJejwvWUI+PEdaRFc+ZUhqbm1vVGxzSS9vZ1l6bGtaZz08L0daRFc+PERaWUo+TlRVNE5ESTFPRFUxT0RoQWNYRXVZMjl0PC9EWllKPjxRTFJMWD5NUT09PC9RTFJMWD48UUxCTD5Nakk9PC9RTEJMPjxHWUZTPk1BPT08L0dZRlM+PEdZUUs+NVlXeDVweUo1b09GNVlhMU1qTXlNdz09PC9HWVFLPjxCWj42TCtaNXBpdjVhU0g1ck9vTVRFPTwvQlo+PFlXSD5ORFk1TURBeU1EQXdNakF4TmpBd01ERTFPVFU9PC9ZV0g+PFFTWlQ+TUE9PTwvUVNaVD48QkRDTFg+TVE9PTwvQkRDTFg+PC9RTFJYWD48L1FMUlhYTGlzdD48L0RZQVE+PC9EWUFRTElTVD48WUdESkxJU1Q+PFlHREogbmFtZT0iNmFLRTVaR0s1NW03Nks2dyI+PEJEQ0RZSD5NVE13TVRBMU1EQTJNREF4UjBJd01EQXdNa1l3TURBeE1EQXhNUT09PC9CRENEWUg+PFlHREpaTD5NUT09PC9ZR0RKWkw+PFpMPlFlVzRna0xsakxwRDViQ1A1WXk2UlRZdE15MHlNREU9PC9aTD48R0hZVD5NVEV4PC9HSFlUPjxKWk1KPk1UQXdMakF3PC9KWk1KPjxCRENESlpNSD5NVE15TXpJeU16UXpNalF6TlRVME5UTTA8L0JEQ0RKWk1IPjxESkpHPmVIaDQ1NXFFNTVtNzZLNnc1cHk2NXA2RTwvREpKRz48WVdIPk5EWTVNREF5TURBd01qQXhOakF3TURFMU9UWT08L1lXSD48UVNaVD5NUT09PC9RU1pUPjxRREpHPk1qazRNeTQ1T1E9PTwvUURKRz48WVdSPjVMbUo1WXFoNUxxNk1nPT08L1lXUj48WVdSWkpaTD5NREU9PC9ZV1JaSlpMPjxZV1JaSkg+TXpJNE56WTFNVGs1TURBNE1ERTROell5PC9ZV1JaSkg+PFREU1lRUj41WnlmNVp5dzVMMi81NVNvNXAyRDVMcTY8L1REU1lRUj48RldYWj5NZz09PC9GV1haPjxGV0pHPk1RPT08L0ZXSkc+PFNaQz5NVFU9PC9TWkM+PFpDUz5Nak09PC9aQ1M+PERKTFg+TWpBdzwvREpMWD48REpZWT41NW03Nks2dzVZNmY1WnVnPC9ESllZPjxESlNKPk1qQXhPUzB3TkMwME5TQXhORG93TXpvMU9BPT08L0RKU0o+PERCUj41NW03NTdDLzVMcTY8L0RCUj48WkRETT5SRTB5TVRJejwvWkRETT48UUxSWFhMaXN0PjxRTFJYWCBuYW1lPSI1cDJENVlpcDVMcTY1TCtoNW9HdiI+PEJEQ0RZSD5NVE13TVRBMU1EQTJNREF4UjBJd01EQXdNa1l3TURBeE1EQXhNUT09PC9CRENEWUg+PFNYSD5NUT09PC9TWEg+PFFMUk1DPjZZT2Q1NGFnNWIyazwvUUxSTUM+PEJEQ1FaSD5NVE15TXpJeU16UXpNalF6TlRVME5UTTA8L0JEQ1FaSD48UVpZU1hMSD5NVEV4TVRJeU1RPT08L1FaWVNYTEg+PFNGQ1pSPk1RPT08L1NGQ1pSPjxaSlpMPk1RPT08L1pKWkw+PFpKSD5OREV4TnpJeU1UazVNREE1TWpVMU1URlk8L1pKSD48RlpKRz5lSGg0NVlXczVhNko1cHk2NVlXejwvRlpKRz48U1NIWT5NREl6TVE9PTwvU1NIWT48R0o+TVRReTwvR0o+PEhKU1pTUz5NVEV3TURBdzwvSEpTWlNTPjxYQj5NUT09PC9YQj48REg+TURFd0xUVTRORFExTlRVMjwvREg+PERaPjVZeVg1THFzNWJpQ2RYaDQ1WXk2NTRtYjZLR1g8L0RaPjxZQj5NVEV3TVRJejwvWUI+PEdaRFc+ZUhqbm1vVGxzSS9vZ1l6bGtaZz08L0daRFc+PERaWUo+TlRVNE5ESTFPRFUxT0RoQWNYRXVZMjl0PC9EWllKPjxRTFJMWD5NUT09PC9RTFJMWD48UUxCTD5Nakk9PC9RTEJMPjxHWUZTPk1BPT08L0dZRlM+PEdZUUs+NVlXeDVweUo1b09GNVlhMU1qTXlNdz09PC9HWVFLPjxCWj42TCtaNXBpdjVhU0g1ck9vTVRFPTwvQlo+PFlXSD5ORFk1TURBeU1EQXdNakF4TmpBd01ERTFPVFk9PC9ZV0g+PFFTWlQ+TUE9PTwvUVNaVD48QkRDTFg+TVE9PTwvQkRDTFg+V2tSWFBnPT08L1FMUlhYPjxRTFJYWCBuYW1lPSI1cDJENVlpcDVMcTY1TCtoNW9HdiI+PEJEQ0RZSD5NVE13TVRBMU1EQTJNREF4UjBJd01EQXdNa1l3TURBeE1EQXhNUT09PC9CRENEWUg+PFNYSD5NZz09PC9TWEg+PFFMUk1DPjVZdSs1N3VONXBtbzwvUUxSTUM+PEJEQ1FaSD5NemMyTlRVeU56ZzNOalUwTkRNeTwvQkRDUVpIPjxRWllTWExIPk1qSXpNVEl4TVRFeTwvUVpZU1hMSD48U0ZDWlI+TVE9PTwvU0ZDWlI+PFpKWkw+TVE9PTwvWkpaTD48WkpIPk16SXdNVEExTVRrNE9UQXpNVGt4TWpjejwvWkpIPjxGWkpHPmVIaDQ1WVdzNWE2SjVweTY1WVd6PC9GWkpHPjxTU0hZPk1ESXpNUT09PC9TU0hZPjxHSj5NVFF5PC9HSj48SEpTWlNTPk1URXdNREF3PC9ISlNaU1M+PFhCPk1RPT08L1hCPjxESD5NREV3TFRVNE5EUTFOVFUyPC9ESD48RFo+NVl5WDVMcXM1YmlDZFhoNDVZeTY1NG1iNktHWDwvRFo+PFlCPk1URXdNVEl6PC9ZQj48R1pEVz5lSGpubW9UbHNJL29nWXpsa1pnPTwvR1pEVz48RFpZSj5OVFU0TkRJMU9EVTFPRGhBY1hFdVkyOXQ8L0RaWUo+PFFMUkxYPk1RPT08L1FMUkxYPjxRTEJMPk1qST08L1FMQkw+PEdZRlM+TUE9PTwvR1lGUz48R1lRSz41WVd4NXB5SjVvT0Y1WWExTWpNeU13PT08L0dZUUs+PEJaPjZMK1o1cGl2NWFTSDVyT29NVEU9PC9CWj48WVdIPk5EWTVNREF5TURBd01qQXhOakF3TURFMU9UWT08L1lXSD48UVNaVD5NQT09PC9RU1pUPjxCRENMWD5NUT09PC9CRENMWD48L1FMUlhYPjwvUUxSWFhMaXN0PjwvWUdESj48L1lHREpMSVNUPjxDRkRKTElTVD48Q0ZESiBuYW1lPSI1cCtsNWJDQjU1bTc2SzZ3Ij48QkRDRFlIPk1UTXdNVEExTURBMk1EQXhSMEl3TURBd01rWXdNREF4TURBek1RPT08L0JEQ0RZSD48Wkw+UWVXNGdrTGxqTHBENWJDUDVZeTZSVFl0TXkweU1EST08L1pMPjxDRkpHPlFlVzRndVM0cmVlNnArUzZ1dWF3a2VlY2dlZTZxdVdubEE9PTwvQ0ZKRz48Q0ZMWD5NUT09PC9DRkxYPjxDRldIPjVwK2w1YkNCNXBhSDVZKzM8L0NGV0g+PENGUVNTSj5NakF4Tnkwd05DMHhOU0F4TkRvd016bzFPQT09PC9DRlFTU0o+PENGSlNTSj5NakF4T1Mwd05DMHhOU0F4TkRvd016bzFPQT09PC9DRkpTU0o+PERKSkc+ZUhoNDU1cUU1NW03Nks2dzVweTY1cDZFPC9ESkpHPjxZV0g+TkRZNU1EQXlNREF3TWpBeE5qQXdNREUxTlRjPTwvWVdIPjxRU1pUPk1RPT08L1FTWlQ+PEpGWVdIPk5EWTVNREF5TURBd01qQXhOakF3TURFMU9UYz08L0pGWVdIPjxKRkpHPjZLZWo1YkNCNXB5NjVZV3pNakk9PC9KRkpHPjxKRldKPjQ0Q0s2S2VqNWJDQjVwYUg1THUyTVRIamdJcz08L0pGV0o+PEpGV0g+NktlajViQ0I1cGFINVkrM01nPT08L0pGV0g+PEpGREJSPjZLZWo1YkNCNTVtNzU3Qy81THE2PC9KRkRCUj48SkZESlNKPk1qQXhPUzB3TkMweE5TQXhORG93TXpvMU9BPT08L0pGREpTSj48REpTSj5NakF4T1Mwd05DMHdOU0F4TkRvd016bzFPQT09PC9ESlNKPjwvQ0ZESj48L0NGREpMSVNUPjwvQkRDQ1hKRz48L0JEQ0ZLTElTVD48L0RhdGE+PC9NZXNzYWdlPg0K'
		result=self.client.service.feedBdcQL(arg0,arg1)

user_url='http://192.168.1.103:8081/ipJwckWebService/IpConvertData?wsdl'
client=Client(user_url)
# print(client)
cx=ckwwebservicecloud(client)
# cx.cxBdcQL()
cx.feedBdcQL()