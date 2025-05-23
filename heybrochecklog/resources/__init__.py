EAC_RIPLINES = {
    'english': 'EAC extraction logfile from',
    'slovak': 'EAC log súbor extrakcie z',
    'bulgarian': 'Отчет на EAC за извличане, извършено на',
    'swedish': 'EAC extraheringsloggfil från',
    'dutch': 'EAC uitlezen log bestand van',
    'spanish': 'Archivo Log de extracciones desde',
    'italian': 'File di log EAC per l\'estrazione del',
    'german': 'EAC Auslese-Logdatei vom',
    'serbian': 'EAC-ov fajl dnevnika ekstrakcije iz',
    'russian': 'Отчёт EAC об извлечении, выполненном',
    'french': 'Journal d\'extraction EAC depuis',
    'uzbek': 'EAC ajratish logfayli',
    'chinese': 'EAC 抓取日志文件从',
    'polish': 'Sprawozdanie ze zgrywania programem EAC z',
    'czech': 'Protokol extrakce EAC z',
}

DEDUCTIONS = {
    'Read mode': {
        'XLD': ['Ripper mode was not XLD Secure Ripper', 100],
        'Default': ['Read mode was not secure', 20],
    },
    'Accurate stream': ['Accurate stream was not used', 20],
    'Audio cache': ['Audio cache not defeated', 10],
    'C2 pointers': ['C2 pointers were used', 20],
    'Drive offset': ['Incorrect read offset for drive', 5],
    'Combined offset': ['Combined read/write offset cannot be verified', 5],
    'Zero offset': [
        'The drive could not be found in the database; however, an offset '
        'of 0 is rarely correct',
        5,
    ],  # noqa E501
    'Fill missing offset samples with silence': [
        'Missing offset samples not filled up with silence',
        5,
    ],
    'Deleting silent blocks': ['Deletes leading and trailing silent blocks', 5],
    'Null samples': ['Null samples were not used in CRC calculations', 1],
    'Gap handling': ['Gaps were not analyzed and appended', 10],
    'ID3 tags': ['ID3 tags added to FLAC files', 1],
    'AccurateRip': ['AccurateRip was not enabled', 5],
    'Test & Copy': ['Test & Copy was not used', 20],
    'Range rip': ['Range rip detected', 20],
    'EAC 0.95': ['EAC 0.95 log or older', 30],
    'HTOA not ripped twice': ['HTOA was not ripped twice', 10],
    'Improper HTOA extraction': ['HTOA was improperly extracted', 10],
    'CRC mismatch on HTOA extraction': ['CRC mismatch on HTOA extraction', 10],
    'Aborted copy': ['Aborted copy', 100],
    'CRC mismatch': ['CRC mismatch', 30],
    'Timing problem': ['Timing problem', 20],
    'Suspicious position': ['Suspicious position', 20],
    'Missing sample': ['Missing sample', 20],
    'Track gain': ['Track gain was not turned on', 1],
    'Read error': ['Read error', 1],
    'Damaged sector count': ['Damaged sector', 1],
    'Checksum': ['No checksum', 15],
    'Virtual drive': ['Virtual drive was used', 100],
    'CD-R': ['CD-R detected; not a pressed CD', 0],
    'AccurateRip discrepancies': [
        'AccurateRip discrepancies; rip may contain silent errors',
        None,
    ],
    'Normalization': ['Destructive normalization used', 100],
    'Compression offset': ['Ripped with compression offset', 100],
    'Log Checksum Not Match': ['Log checksum does not match', 100]
}

VERSIONS = {
    'EAC': [
        ('V1.8', '15. July 2024'),
        ('V1.7', '14. July 2024'), # This is removed due to bugs, adding support to it nevertheless
        ('V1.6', '23. October 2020'),
        ('V1.5', '20. February 2020'),
        ('V1.4', '3. February 2020'),
        ('V1.3', '2. September 2016'),
        ('V1.2', '12. August 2016'),
        ('V1.1', '23. June 2015'),
        ('V1.0 beta 6', '9. April 2015'),
        ('V1.0 beta 5', '2. April 2015'),
        ('V1.0 beta 4', '7. December 2014'),
        ('V1.0 beta 3', '29. August 2011'),
        ('V1.0 beta 2', '29. April 2011'),
        ('V1.0 beta 1', '15. November 2010'),
        ('V0.99 prebeta 5', '4. May 2009'),
        ('V0.99 prebeta 4', '23. January 2008'),
        ('V0.99 prebeta 3', '28. July 2007'),
        ('V0.99 prebeta 2', '28 July 2007'),
        ('V0.99 prebeta 1', '25. May 2007'),
        ('EAC <=0.95', '1. April 1970'),
    ],
    'XLD': [
        ('20250302', '157.2'),
        ('20240511', '157.1'),
        ('20240310', '157.0'),
        ('20230627', '156.1'),
        ('20230416', '156.0'),
        ('20220917', '155.1'),
        ('20220910', '155.0'),
        ('20211018', '154.0'),
        ('20210101', '153.1'),
        ('20201123', '153.0'),
        ('20191004', '152.0'),
        ('20181019', '151.1'),
        ('20170729', '150.3'),
        ('20170710', '150.2'),
        ('20161007', '149.3'),
        ('20160920', '149.2'),
        ('20151214', '149.1'),
        ('20151128', '149.0'),
        ('20141129a', '148.2'),
        ('20141129', '148.1'),
        ('20141109', '148.0'),
        ('20140504', '147.0'),
        ('20140427', '146.0'),
        ('20131102', '145.0'),
        ('20130720', '144.0'),
        ('20130602', '143.2'),
        ('20130601', '143.1'),
        ('20130407', '143.0'),
        ('20130127', '142.3'),
        ('20121222', '142.2'),
        ('20121027', '142.1'),
        ('20121013', '142.0'),
        ('20120908', '141.1'),
        ('20120609', '141.0'),
        ('20120407', '140.0'),
        ('20120226', '139.1'),
        ('20120120', '139.0'),
        ('20111214', '138.1'),
        ('20111211', '138.0'),
        ('20111113', '137.1'),
        ('20111113', '137.0'),
        ('20111015', '136.4'),
        ('20110924', '136.3'),
        ('20110821', '136.1'),
        ('20110820', '136.0'),
        ('20110703', '135.1'),
        ('20110611', '135.0'),
        ('20110528', '134.0'),
        ('20110515', '133.1'),
        ('20110508', '133.0'),
        ('20110502', '132.0'),
        ('20110417', '131.0'),
        ('20110312', '130.0'),
        ('20110228', '129.0'),
        ('20110226', '128.0'),
        ('20110212', '127.0'),
        ('20101212', '126.2'),
        ('20101208', '126.1'),
        ('20101128', '126.0'),
        ('20101120', '125.2'),
        ('20101117', '125.1'),
        ('20101115', '125.0'),
        ('20101107', '124.1'),
        ('20101107', '124.0'),
        ('20101031', '123.7'),
        ('20101027', '123.6'),
        ('20101023', '123.5'),
        ('20101023', '123.4'),
        ('20101010', '123.3'),
        ('20100926', '123.1'),
        ('20100926', '123.0'),
        ('20100918', '122.1'),
        ('20100911', '122.0'),
        ('20100908', '121.2'),
        ('20100907', '121.1'),
        ('20100907', '121.0'),
        ('20100904', '120.7'),
        ('20100828', '120.6'),
        ('20100711', '120.5'),
        ('20100704', '120.4'),
        ('20100518', '120.3'),
        ('20100516', '120.2'),
        ('20100515', '119.3'),
        ('20100511', '119.2'),
        ('20100505', '119.1'),
        ('20100503', '119.0'),
        ('20100424', '118.0'),
        ('20100417', '117.4'),
        ('20100412', '117.3'),
        ('20100409', '117.2'),
        ('20100401', '117.0'),
        ('20100323', '116.7'),
        ('20100302', '116.6'),
        ('20100301', '116.5'),
        ('20100218', '116.4'),
        ('20100217', '116.3'),
        ('20100214', '116.2'),
        ('20100209', '116.0'),
        ('20100206', '115.6'),
        ('20100205', '115.5'),
        ('20100123', '115.4'),
        ('20100117', '115.3'),
        ('20091230', '115.2'),
        ('20091225', '115.1'),
        ('20091223', '115.0'),
        ('20091212', '114.6'),
        ('20091202', '114.5'),
        ('20091202', '114.4'),
        ('20091129', '114.3'),
        ('20091127', '114.2'),
        ('20091125', '114.1'),
        ('20091123', '114.0'),
        ('20091121', '113.4'),
        ('20091115', '113.3'),
        ('20091114', '113.2'),
        ('20091112', '113.1'),
        ('20091111', '113.0'),
        ('20091108', '112.0'),
        ('20091107', '111.0'),
        ('20090930', '110.0'),
        ('20090924', '109.9'),
        ('20090922', '109.8'),
        ('20090910', '109.7'),
        ('20090829', '109.6'),
        ('20090828', '109.5'),
        ('20090827a', '109.4'),
        ('20090824a', '109.2'),
        ('20090824', '109.1'),
        ('20090320', '105.1'),
        ('20090318', '105.0'),
        ('20090317', '104.4'),
        ('20090315a', '104.3'),
        ('20090315', '104.2'),
        ('20090314', '104.1'),
        ('20090217', '101.1'),
        ('20090215', '100.1'),
        ('20080926', '93.3'),
        ('20080925', '93.2'),
        ('20080921', '92.1'),
        ('20080916c', '91.3'),
        ('20080914a', '90.1'),
        ('86.1', '20080907a'),
    ],
}
