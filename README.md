# Domainlists.io Downloader  
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)
[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)  
*A simple Python script used to download lists from [Domainlists.io](https://domainlists.io/)*  

## DOMAINLISTS.IO API description
*For power users and developers. Use it for batch domain lists downloads.*

### Send simple GET-request to `https://domainlists.io/api/`

API requires an active [PRO plan subscription](https://domainlists.io/#pricing)!

### Overview

#### Request format

`https://domainlists.io/api/LIST_TYPE/ZONE_CODE/YOUR_LOGIN/YOUR_PASSWORD/`

#### Results
If everything is correct, API returns:  
for `domains lists`: the requested list in plain text format (1 domain per line)  
for `domains + DNS lists`: the requested list with domain name and pipe delimited DNS servers: domain.tld, DNS1|DNS2|DNS3|etc.  

In case of error you'll get an error description in plain text:  
`Incorrect username or password`  
`Paid subscription required`  
`Incorrect list type`  
`Incorrect zone id`  

#### Limits & warnings
API requires an active subscription ([PRO plan](https://domainlists.io/#pricing)).  
You can call API methods a maximum of 3000 times per day.  
Some of the domain lists are really HUGE. The size of the 'all-in-one' zone file is about 3 Gb.  

### Variables  

#### YOUR_LOGIN, YOUR_PASSWORD  
`YOUR_LOGIN` - your login on DOMAINLISTS.IO (usually your email address)  
`YOUR_PASSWORD` - your password on DOMAINLISTS.IO  

#### LIST_TYPE (list types):  
`full` - full list of domains  
`new` - list of new (added today) domains (for generic zones only)  
`deleted` - list of deleted (removed today) domains (for generic zones only)  
`fulldns` - full list of domains + DNS  
`newdns` - list of new (added today) domains + DNS (for generic zones only)  
`deleteddns` - list of deleted (removed today) domains + DNS (for generic zones only)  


##### List all currently available TLDs with stats
You can list all the currently supported TLDs in our database with statistics like:  
*Total Websites*, *New Websites*, *Deleted Websites*, *ID of TLD* and *TLD name*.

Endpoint: `https://domainlists.io/api/tlds/list/EMAIL/PASS/`

*Note: you can list just Top 5 TLDs per category by passing querystring like:* 
`https://domainlists.io/api/tlds/list/EMAIL/PASS/?top`

#### ZONE_CODE (domain TLD IDs):

| TLD name  | ZONE_CODE |
| --- | --- |
|ALL DOMAINS|all_zones|
|.biz	|532
|.com	|534
|.info	|535
|.net	|537
|.org	|538
|.gratis	|1
|.insure	|2
|.investments	|3
|.limited	|4
|.wtc	|5
|.airforce	|6
|.accountants	|7
|.claims	|8
|.credit	|9
|.digital	|10
|.foo	|11
|.schule	|12
|.soy	|13
|.surgery	|14
|.tax	|15
|.wtf	|16
|.luxe	|17
|.guide	|18
|.audio	|19
|.hiphop	|20
|.loans	|21
|.church	|22
|.life	|23
|.beer	|24
|.juegos	|25
|.rio	|26
|.reise	|27
|.xn--4gbrim	|28
|.engineer	|29
|.attorney	|30
|.xn--kput3i	|31
|.vlaanderen	|32
|.brussels	|33
|.green	|34
|.capetown	|35
|.durban	|36
|.joburg	|37
|.lotto	|38
|.organic	|39
|.direct	|40
|.place	|41
|.surf	|42
|.army	|43
|.gives	|44
|.navy	|45
|.rehab	|46
|.republican	|47
|.city	|48
|.cuisinella	|49
|.deals	|50
|.degree	|51
|.dentist	|52
|.lawyer	|53
|.market	|54
|.mortgage	|55
|.xn--unup4y	|56
|.software	|57
|.vet	|58
|.krd	|59
|.lgbt	|60
|.ngo	|61
|.ong	|62
|.nra	|63
|.gent	|64
|.nrw	|65
|.whoswho	|66
|.gifts	|67
|.healthcare	|68
|.auction	|69
|.restaurant	|70
|.sarl	|71
|.cern	|72
|.click	|73
|.diet	|74
|.help	|75
|.hosting	|76
|.how	|77
|.ltda	|78
|.property	|79
|.schmidt	|80
|.top	|81
|.uol	|82
|.boo	|83
|.dad	|84
|.day	|85
|.eat	|86
|.esq	|87
|.gbiz	|88
|.gmail	|89
|.here	|90
|.ing	|91
|.meme	|92
|.mov	|93
|.new	|94
|.prod	|95
|.rsvp	|96
|.youtube	|97
|.business	|98
|.immo	|99
|.network	|100
|.ooo	|101
|.pizza	|102
|.xn--vhquv	|103
|.xn--1qqw23a	|104
|.cal	|105
|.channel	|106
|.chrome	|107
|.fly	|108
|.gle	|109
|.google	|110
|.nexus	|111
|.prof	|112
|.zip	|113
|.world	|114
|.budapest	|115
|.casa	|116
|.work	|117
|.forsale	|118
|.band	|119
|.ibm	|120
|.poker	|121
|.abogado	|122
|.rip	|123
|.ventures	|124
|.delivery	|125
|.energy	|126
|.equipment	|127
|.xn--xhq521b	|128
|.android	|129
|.science	|130
|.singles	|131
|.cricket	|132
|.party	|133
|.wedding	|134
|.yoga	|135
|.xn--flw351e	|136
|.xn--qcka1pmc	|137
|.lighting	|138
|.coach	|139
|.irish	|140
|.latrobe	|141
|.holdings	|142
|.legal	|143
|.madrid	|144
|.memorial	|145
|.money	|146
|.voyage	|147
|.xn--czrs0t	|148
|.tires	|149
|.clothing	|150
|.dev	|151
|.docs	|152
|.sale	|153
|.video	|154
|.fashion	|155
|.garden	|156
|.guru	|157
|.samsung	|158
|.xn--hxt814e	|159
|.flowers	|160
|.bike	|161
|.fit	|162
|.xn--45q11c	|163
|.amsterdam	|164
|.camera	|165
|.lidl	|166
|.barclays	|167
|.dabur	|168
|.dclk	|169
|.goog	|170
|.hangout	|171
|.temasek	|172
|.xn--b4w605ferd	|173
|.one	|174
|.everbank	|175
|.kyoto	|176
|.construction	|177
|.design	|178
|.lat	|179
|.ntt	|180
|.bingo	|181
|.contractors	|182
|.bloomberg	|183
|.chat	|184
|.style	|185
|.tennis	|186
|.estate	|187
|.hermes	|188
|.apartments	|189
|.saxo	|190
|.gallery	|191
|.cbn	|192
|.schwarz	|193
|.casino	|194
|.graphics	|195
|.football	|196
|.school	|197
|.shriram	|198
|.land	|199
|.plumbing	|200
|.trust	|201
|.oracle	|202
|.leclerc	|203
|.java	|204
|.page	|205
|.ads	|206
|.gold	|207
|.golf	|208
|.guge	|209
|.plus	|210
|.tours	|211
|.news	|212
|.accountant	|213
|.date	|214
|.download	|215
|.faith	|216
|.loan	|217
|.movie	|218
|.afl	|219
|.sexy	|220
|.bond	|221
|.review	|222
|.win	|223
|.xn--30rr7y	|224
|.tattoo	|225
|.xn--9et52u	|226
|.xn--nyqy26a	|227
|.racing	|228
|.technology	|229
|.cafe	|230
|.express	|231
|.diamonds	|232
|.mma	|233
|.xn--kcrx77d1x4a	|234
|.jewelry	|235
|.show	|236
|.directory	|237
|.team	|238
|.enterprises	|239
|.dog	|240
|.kitchen	|241
|.photography	|242
|.tips	|243
|.icu	|244
|.cfa	|245
|.theater	|246
|.hockey	|247
|.xn--q9jyb4c	|248
|.run	|249
|.taxi	|250
|.philips	|251
|.xn--fjq720a	|252
|.accenture	|253
|.coupons	|254
|.soccer	|255
|.men	|256
|.fyi	|257
|.mba	|258
|.thd	|259
|.sandvik	|260
|.sandvikcoromant	|261
|.walter	|262
|.lol	|263
|.auto	|264
|.cars	|265
|.homedepot	|266
|.jll	|267
|.lasalle	|268
|.drive	|269
|.genting	|270
|.play	|271
|.starhub	|272
|.vista	|273
|.vistaprint	|274
|.scor	|275
|.today	|276
|.cloud	|277
|.hoteles	|278
|.law	|279
|.movistar	|280
|.telefonica	|281
|.live	|282
|.studio	|283
|.sakura	|284
|.bradesco	|285
|.app	|286
|.ubs	|287
|.lancaster	|288
|.bet	|289
|.srl	|290
|.game	|291
|.pet	|292
|.xn--11b4c3d	|293
|.xn--3pxu8k	|294
|.xn--42c2d9a	|295
|.xn--9dbq2a	|296
|.xn--c2br7g	|297
|.xn--fhbei	|298
|.xn--j1aef	|299
|.xn--mk1bu44c	|300
|.xn--pssy2u	|301
|.xn--t60b56a	|302
|.xn--tckwe	|303
|.boots	|304
|.vin	|305
|.wine	|306
|.immobilien	|307
|.family	|308
|.group	|309
|.seek	|310
|.email	|311
|.giving	|312
|.chanel	|313
|.fage	|314
|.mom	|315
|.solutions	|316
|.xn--efvy88h	|317
|.car	|318
|.stada	|319
|.bms	|320
|.ltd	|321
|.obi	|322
|.holiday	|323
|.bom	|324
|.final	|325
|.seven	|326
|.stockholm	|327
|.mtr	|328
|.florist	|329
|.coffee	|330
|.meo	|331
|.sapo	|332
|.sbs	|333
|.builders	|334
|.jobs	|335
|.creditunion	|336
|.tab	|337
|.comsec	|338
|.broadway	|339
|.repair	|340
|.verisign	|341
|.vip	|342
|.ninja	|343
|.kaufen	|344
|.house	|345
|.salon	|346
|.training	|347
|.travelers	|348
|.redumbrella	|349
|.trv	|350
|.kpn	|351
|.travelersinsurance	|352
|.codes	|353
|.international	|354
|.lamer	|355
|.origins	|356
|.promo	|357
|.onl	|358
|.clinique	|359
|.baidu	|360
|.weather	|361
|.glass	|362
|.xn--g2xx48c	|363
|.education	|364
|.pamperedchef	|365
|.adac	|366
|.nikon	|367
|.weatherchannel	|368
|.quest	|369
|.gallup	|370
|.farm	|371
|.pwc	|372
|.natura	|373
|.solar	|374
|.hiv	|375
|.institute	|376
|.passagens	|377
|.vuelos	|378
|.kerrylogistics	|379
|.kerryhotels	|380
|.kerryproperties	|381
|.kuokgroup	|382
|.xn--w4r85el8fhu5dnra	|383
|.avianca	|384
|.gmbh	|385
|.barclaycard	|386
|.stream	|387
|.bcg	|388
|.nissay	|389
|.recipes	|390
|.computer	|391
|.academy	|392
|.careers	|393
|.cab	|394
|.systems	|395
|.domains	|396
|.viajes	|397
|.company	|398
|.camp	|399
|.limo	|400
|.management	|401
|.photos	|402
|.shoes	|403
|.center	|404
|.buzz	|405
|.support	|406
|.xn--3bst00m	|407
|.xn--6qq986b3xl	|408
|.wang	|409
|.dance	|410
|.moda	|411
|.agency	|412
|.social	|413
|.democrat	|414
|.marketing	|415
|.cheap	|416
|.zone	|417
|.pics	|418
|.pink	|419
|.photo	|420
|.gift	|421
|.rich	|422
|.red	|423
|.shiksha	|424
|.xn--fiq64b	|425
|.link	|426
|.guitars	|427
|.tools	|428
|.cool	|429
|.kim	|430
|.watch	|431
|.expert	|432
|.works	|433
|.tienda	|434
|.bargains	|435
|.boutique	|436
|.community	|437
|.dating	|438
|.catering	|439
|.cleaning	|440
|.cruises	|441
|.events	|442
|.exposed	|443
|.flights	|444
|.partners	|445
|.properties	|446
|.rentals	|447
|.report	|448
|.blue	|449
|.xn--6frz82g	|450
|.vision	|451
|.cards	|452
|.foundation	|453
|.condos	|454
|.villas	|455
|.parts	|456
|.productions	|457
|.maison	|458
|.qpon	|459
|.supplies	|460
|.fish	|461
|.xn--cg4bki	|462
|.vacations	|463
|.industries	|464
|.supply	|465
|.wiki	|466
|.actor	|467
|.pub	|468
|.christmas	|469
|.voto	|470
|.vote	|471
|.bid	|472
|.koeln	|473
|.xn--c1avg	|474
|.xn--nqv7f	|475
|.xn--i1b6b1a6a2e	|476
|.xn--nqv7fs00ema	|477
|.xn--rhqv96g	|478
|.ink	|479
|.london	|480
|.black	|481
|.meet	|482
|.ren	|483
|.webcam	|484
|.trade	|485
|.cologne	|486
|.vodka	|487
|.cooking	|488
|.rodeo	|489
|.country	|490
|.xn--czru2d	|491
|.horse	|492
|.fishing	|493
|.miami	|494
|.futbol	|495
|.reviews	|496
|.rocks	|497
|.haus	|498
|.consulting	|499
|.saarland	|500
|.gop	|501
|.capital	|502
|.gripe	|503
|.engineering	|504
|.services	|505
|.lease	|506
|.toys	|507
|.town	|508
|.career	|509
|.media	|510
|.reisen	|511
|.associates	|512
|.university	|513
|.pictures	|514
|.blackfriday	|515
|.care	|516
|.cash	|517
|.clinic	|518
|.dental	|519
|.discount	|520
|.exchange	|521
|.fail	|522
|.bayern	|523
|.citic	|524
|.creditcard	|525
|.finance	|526
|.financial	|527
|.fitness	|528
|.fund	|529
|.furniture	|530
|.globo	|531
|.mobi	|536
|.us	|539
|.xxx	|540
|.gmo	|541
|.nhk	|542
|.ovh	|543
|.tirol	|544
|.suzuki	|545
|.xn--ngbc5azd	|546
|.cancerresearch	|547
|.melbourne	|548
|.caravan	|549
|.otsuka	|550
|.yandex	|551
|.sydney	|552
|.reit	|553
|.wme	|554
|.kddi	|555
|.ggee	|556
|.lotte	|557
|.mormon	|558
|.lds	|559
|.jcb	|560
|.canon	|561
|.toshiba	|562
|.nico	|563
|.fans	|564
|.goldpoint	|565
|.yodobashi	|566
|.courses	|567
|.study	|568
|.goo	|569
|.datsun	|570
|.infiniti	|571
|.mtpc	|572
|.nissan	|573
|.fan	|574
|.coop	|575
|.tech	|576
|.film	|577
|.tickets	|578
|.hitachi	|579
|.rent	|580
|.menu	|581
|.forum	|582
|.realty	|583
|.stcgroup	|584
|.viva	|585
|.stc	|586
|.protection	|587
|.theatre	|588
|.security	|589
|.kfh	|590
|.xn--ngbe9e0a	|591
|.contact	|592
|.pid	|593
|.health	|594
|.tvs	|595
|.ruhr	|596
|.monash	|597
|.nagoya	|598
|.tokyo	|599
|.xyz	|600
|.bar	|601
|.okinawa	|602
|.dnp	|603
|.rest	|604
|.ryukyu	|605
|.yokohama	|606
|.feedback	|607
|.college	|608
|.cymru	|610
|.wales	|611
|.osaka	|612
|.xin	|613
|.redstone	|614
|.sap	|615
|.cyou	|616
|.xn--estv75g	|617
|.icbc	|618
|.earth	|619
|.sohu	|620
|.moe	|621
|.eus	|622
|.quebec	|623
|.bio	|624
|.bmw	|625
|.mini	|626
|.spiegel	|627
|.allfinanz	|628
|.dvag	|629
|.emerck	|630
|.flsmidth	|631
|.pohl	|632
|.tui	|633
|.xn--vermgensberater-ctb	|634
|.xn--vermgensberatung-pwb	|635
|.zuerich	|636
|.ski	|637
|.itau	|638
|.mutuelle	|639
|.bostik	|640
|.sfr	|641
|.fresenius	|642
|.total	|643
|.archi	|644
|.abbott	|645
|.bauhaus	|646
|.cisco	|647
|.dell	|648
|.lifeinsurance	|649
|.makeup	|650
|.skin	|651
|.sew	|652
|.versicherung	|653
|.active	|654
|.realtor	|655
|.marriott	|656
|.eurovision	|657
|.bible	|658
|.barcelona	|659
|.bcn	|660
|.amica	|661
|.fairwinds	|662
|.grainger	|663
|.cat	|664
|.safety	|665
|.storage	|666
|.tiffany	|667
|.extraspace	|668
|.wien	|669
|.xn--io0a7i	|670
|.xn--55qx5d	|671
|.mobily	|673
|.xn--mgbb9fbpob	|674
|.edu	|675
|.hamburg	|676
|.crs	|677
|.aquarelle	|678
|.bank	|679
|.cfd	|680
|.forex	|681
|.markets	|682
|.spreadbetting	|683
|.trading	|684
|.doha	|685
|.broker	|686
|.nadex	|687
|.liaison	|688
|.jprs	|689
|.delta	|690
|.aramco	|691
|.xn--mgba3a3ejt	|692
|.insurance	|693
|.med	|694
|.ceo	|695
|.best	|696
|.kred	|697
|.norton	|698
|.symantec	|699
|.museum	|700
|.vegas	|701
|.dubai	|702
|.erni	|703
|.ice	|704
|.cityeats	|705
|.lifestyle	|706
|.vana	|707
|.living	|708
|.viking	|709
|.praxi	|710
|.scb	|711
|.adult	|712
|.porn	|713
|.sex	|714
|.abb	|715
|.aig	|716
|.wed	|717
|.williamhill	|718
|.frl	|719
|.firmdale	|720
|.rf	|722
|.ru	|723
|.su	|724
|.desi	|725
|.xerox	|726
|.aarp	|727
|.locus	|728
|.star	|729
|.yachts	|730
|.autos	|731
|.motorcycles	|732
|.homes	|733
|.boats	|734
|.paris	|735
|.love	|736
|.luxury	|737
|.ipiranga	|738
|.aco	|739
|.gea	|740
|.analytics	|741
|.jmp	|742
|.apple	|743
|.beats	|744
|.schaeffler	|745
|.sas	|746
|.xn--80aswg	|747
|.scot	|748
|.lacaixa	|749
|.xn--80asehdb	|750
|.seat	|751
|.xn--mgbab2bd	|752
|.mango	|753
|.gal	|754
|.mtn	|755
|.ping	|756
|.xn--czr694b	|757
|.xn--imr513n	|758
|.ist	|759
|.istanbul	|760
|.sina	|761
|.aaa	|762
|.abbvie	|763
|.abudhabi	|764
|.ac	|765
|.ad	|766
|.ae	|767
|.aeg	|768
|.aero	|769
|.af	|770
|.ag	|771
|.agakhan	|772
|.ai	|773
|.airtel	|774
|.akdn	|775
|.al	|776
|.alibaba	|777
|.alipay	|778
|.ally	|779
|.alsace	|780
|.am	|781
|.an	|782
|.anquan	|783
|.ao	|784
|.aq	|785
|.ar	|786
|.arpa	|787
|.arte	|788
|.as	|789
|.asia	|790
|.at	|791
|.au	|792
|.audi	|793
|.author	|794
|.aw	|795
|.aws	|796
|.ax	|797
|.axa	|798
|.az	|799
|.azure	|800
|.ba	|801
|.baby	|802
|.barefoot	|803
|.bb	|804
|.bbc	|805
|.bbva	|806
|.bd	|807
|.be	|808
|.bentley	|809
|.berlin	|810
|.bf	|811
|.bg	|812
|.bh	|813
|.bharti	|814
|.bi	|815
|.bing	|816
|.bj	|817
|.bl	|818
|.bm	|819
|.bn	|820
|.bnl	|821
|.bnpparibas	|822
|.bo	|823
|.boehringer	|824
|.book	|825
|.bosch	|826
|.bot	|827
|.bq	|828
|.br	|829
|.bridgestone	|830
|.brother	|831
|.bs	|832
|.bt	|833
|.bugatti	|834
|.build	|835
|.buy	|836
|.bv	|837
|.bw	|838
|.by	|839
|.bz	|840
|.bzh	|841
|.ca	|842
|.call	|843
|.cartier	|844
|.cba	|845
|.cc	|846
|.cd	|847
|.ceb	|848
|.cf	|849
|.cg	|850
|.ch	|851
|.chase	|852
|.chloe	|853
|.ci	|854
|.cipriani	|855
|.circle	|856
|.ck	|857
|.cl	|858
|.club	|859
|.clubmed	|860
|.cm	|861
|.cn	|862
|.co	|863
|.commbank	|864
|.compare	|865
|.corsica	|866
|.coupon	|867
|.cr	|868
|.crown	|869
|.csc	|870
|.cu	|871
|.cv	|872
|.cw	|873
|.cx	|874
|.cy	|875
|.cz	|876
|.dds	|877
|.de	|878
|.dealer	|879
|.deloitte	|880
|.dj	|881
|.dk	|882
|.dm	|883
|.do	|884
|.doosan	|885
|.dz	|886
|.ec	|887
|.edeka	|888
|.ee	|889
|.eg	|890
|.eh	|891
|.epson	|892
|.er	|893
|.es	|894
|.et	|895
|.eu	|896
|.fast	|897
|.ferrero	|898
|.fi	|899
|.firestone	|900
|.fj	|901
|.fk	|902
|.flickr	|903
|.fm	|904
|.fo	|905
|.ford	|906
|.fox	|907
|.fr	|908
|.frogans	|909
|.frontier	|910
|.ftr	|911
|.ga	|912
|.gallo	|913
|.gb	|914
|.gd	|915
|.gdn	|916
|.ge	|917
|.gf	|918
|.gg	|919
|.gh	|920
|.gi	|921
|.gl	|922
|.global	|923
|.gm	|924
|.gmx	|925
|.gn	|926
|.got	|927
|.gov	|928
|.gp	|929
|.gq	|930
|.gr	|931
|.gs	|932
|.gt	|933
|.gu	|934
|.gucci	|935
|.gw	|936
|.gy	|937
|.hdfcbank	|938
|.helsinki	|939
|.hk	|940
|.hkt	|941
|.hm	|942
|.hn	|943
|.honda	|944
|.host	|945
|.hotmail	|946
|.hr	|947
|.hsbc	|948
|.ht	|949
|.htc	|950
|.hu	|951
|.hyundai	|952
|.id	|953
|.ie	|954
|.ifm	|955
|.iinet	|956
|.il	|957
|.im	|958
|.imamat	|959
|.in	|960
|.int	|961
|.io	|962
|.iq	|963
|.ir	|964
|.is	|965
|.iselect	|966
|.ismaili	|967
|.it	|968
|.iwc	|969
|.jaguar	|970
|.jcp	|971
|.je	|972
|.jetzt	|973
|.jlc	|974
|.jm	|975
|.jnj	|976
|.jo	|977
|.jot	|978
|.joy	|979
|.jp	|980
|.jpmorgan	|981
|.ke	|982
|.kg	|983
|.kh	|984
|.ki	|985
|.kia	|986
|.kinder	|987
|.kiwi	|988
|.km	|989
|.kn	|990
|.komatsu	|991
|.kp	|992
|.kpmg	|993
|.kr	|994
|.kw	|995
|.ky	|996
|.kz	|997
|.la	|998
|.lamborghini	|999
|.landrover	|1000
|.lanxess	|1001
|.lb	|1002
|.lc	|1003
|.lexus	|1004
|.li	|1005
|.like	|1006
|.lincoln	|1007
|.linde	|1008
|.lipsy	|1009
|.lixil	|1010
|.lk	|1011
|.lr	|1012
|.ls	|1013
|.lt	|1014
|.lu	|1015
|.lupin	|1016
|.lv	|1017
|.ly	|1018
|.ma	|1019
|.maif	|1020
|.man	|1021
|.mc	|1022
|.md	|1023
|.me	|1024
|.mf	|1025
|.mg	|1026
|.mh	|1027
|.microsoft	|1028
|.mil	|1029
|.mk	|1030
|.ml	|1031
|.mls	|1032
|.mm	|1033
|.mn	|1034
|.mo	|1035
|.moi	|1036
|.montblanc	|1037
|.moscow	|1038
|.mp	|1039
|.mq	|1040
|.mr	|1041
|.ms	|1042
|.mt	|1043
|.mu	|1044
|.mutual	|1045
|.mv	|1046
|.mw	|1047
|.mx	|1048
|.my	|1049
|.mz	|1050
|.na	|1051
|.name	|1052
|.nc	|1053
|.ne	|1054
|.nec	|1055
|.netbank	|1056
|.neustar	|1057
|.next	|1058
|.nextdirect	|1059
|.nf	|1060
|.ng	|1061
|.ni	|1062
|.nl	|1063
|.no	|1064
|.nokia	|1065
|.northwesternmutual	|1066
|.nowruz	|1067
|.nowtv	|1068
|.np	|1069
|.nr	|1070
|.nu	|1071
|.nyc	|1072
|.nz	|1073
|.office	|1074
|.olayan	|1075
|.olayangroup	|1076
|.om	|1077
|.omega	|1078
|.online	|1079
|.orange	|1080
|.pa	|1081
|.panerai	|1082
|.pars	|1083
|.pe	|1084
|.pf	|1085
|.pg	|1086
|.ph	|1087
|.pharmacy	|1088
|.physio	|1089
|.piaget	|1090
|.pictet	|1091
|.pin	|1092
|.pk	|1093
|.pl	|1094
|.playstation	|1095
|.pm	|1096
|.pn	|1097
|.post	|1098
|.pr	|1099
|.press	|1100
|.pro	|1101
|.progressive	|1102
|.ps	|1103
|.pt	|1104
|.pw	|1105
|.py	|1106
|.qa	|1107
|.re	|1108
|.read	|1109
|.rexroth	|1110
|.ricoh	|1111
|.ro	|1112
|.rocher	|1113
|.room	|1114
|.rs	|1115
|.rw	|1116
|.rwe	|1117
|.sa	|1118
|.safe	|1119
|.sanofi	|1120
|.sb	|1121
|.sbi	|1122
|.sc	|1123
|.sca	|1124
|.scholarships	|1125
|.sd	|1126
|.se	|1127
|.select	|1128
|.sener	|1129
|.sg	|1130
|.sh	|1131
|.sharp	|1132
|.shaw	|1133
|.shell	|1134
|.shia	|1135
|.shouji	|1136
|.si	|1137
|.site	|1138
|.sj	|1139
|.sk	|1140
|.sky	|1141
|.skype	|1142
|.sl	|1143
|.sm	|1144
|.smile	|1145
|.sn	|1146
|.sncf	|1147
|.so	|1148
|.softbank	|1149
|.song	|1150
|.sony	|1151
|.space	|1152
|.spot	|1153
|.sr	|1154
|.ss	|1155
|.st	|1156
|.statebank	|1157
|.statefarm	|1158
|.statoil	|1159
|.store	|1160
|.sucks	|1161
|.sv	|1162
|.swatch	|1163
|.swiss	|1164
|.sx	|1165
|.sy	|1166
|.sz	|1167
|.taipei	|1168
|.talk	|1169
|.taobao	|1170
|.tatamotors	|1171
|.tatar	|1172
|.tc	||1173
|.tci	|1174
|.td	|1175
|.tel	|1176
|.telecity	|1177
|.teva	|1178
|.tf	|1179
|.tg	|1180
|.th	|1181
|.tj	|1182
|.tk	|1183
|.tl	|1184
|.tm	|1185
|.tmall	|1186
|.tn	|1187
|.to	|1188
|.toray	|1189
|.toyota	|1190
|.tp	|1191
|.tr	|1192
|.travel	|1193
|.tt	|1194
|.tube	|1195
|.tunes	|1196
|.tushu	|1197
|.tv	|1198
|.tw	|1199
|.tz	|1200
|.ua	|1201
|.ug	|1202
|.uk	|1203
|.um	|1204
|.unicom	|1205
|.uno	|1206
|.uy	|1207
|.uz	|1208
|.va	|1209
|.vc	|1210
|.ve	|1211
|.vg	|1212
|.vi	|1213
|.vig	|1214
|.virgin	|1215
|.vn	|1216
|.volkswagen	|1217
|.voting	|1218
|.vu	|1219
|.wanggou	|1220
|.warman	|1221
|.watches	|1222
|.weber	|1223
|.website	|1224
|.weibo	|1225
|.weir	|1226
|.wf	|1227
|.windows	|1228
|.wolterskluwer	|1229
|.ws	|1230
|.xbox	|1231
|.xihuan	|1232
|.测试	|1233
|.कॉम	|1234
|.परीक्षा	|1235
|.セール	|1236
|.佛山	|1237
|.ಭಾರತ	|1238
|.慈善	|1239
|.集团	|1240
|.在线	|1241
|.한국	|1242
|.ଭାରତ	|1243
|.点看	|1244
|.คอม	|1245
|.ভাৰত	|1246
|.ভারত	|1247
|.八卦	|1248
|.বাংলা	|1250
|.公益	|1251
|.公司	|1252
|.网站	|1253
|.移动	|1254
|.我爱你	|1255
|.москва	|1256
|.испытание	|1257
|.қаз	|1258
|.онлайн	|1259
|.сайт	|1260
|.联通	|1261
|.срб	|1262
|.бг	|1263
|.бел	|1264
|.时尚	|1266
|.微博	|1267
|.테스트	|1268
|.淡马锡	|1269
|.ファッション	|1270
|.орг	|1271
|.नेट	|1272
|.ストア	|1273
|.삼성	|1274
|.சிங்கப்பூர்	|1275
|.商标	|1276
|.商店	|1277
|.商城	|1278
|.дети	|1279
|.мкд	|1280
|.ею	|1282
|.ポイント	|1283
|.新闻	|1284
|.工行	|1285
|.家電	|1286
|.中文网	|1288
|.中信	|1289
|.中国	|1290
|.中國	|1291
|.娱乐	|1292
|.谷歌	|1293
|.భారత్	|1294
|.ලංකා	|1295
|.购物	|1296
|.測試	|1297
|.クラウド	|1298
|.ભારત	|1299
|.भारत	|1300
|.பரிட்சை	|1302
|.网店	|1303
|.संगठन	|1304
|.餐厅	|1305
|.网络	|1306
|.ком	|1307
|.укр	|1308
|.香港	|1309
|.诺基亚	|1310
|.食品	|1311
|.δοκιμή	|1312
|.飞利浦	|1313
|.台湾	|1315
|.台灣	|1316
|.手表	|1317
|.手机	|1318
|.мон	|1319
|.澳門	|1338
|.닷컴	|1339
|.政府	|1340
|.გე	|1343
|.机构	|1344
|.组织机构	|1345
|.健康	|1346
|.ไทย	|1347
|.рус	|1349
|.рф	|1350
|.珠宝	|1351
|.大拿	|1353
|.みんな	|1354
|.グーグル	|1355
|.ελ	|1356
|.世界	|1357
|.書籍	|1358
|.ഭാരതം	|1359
|.ਭਾਰਤ	|1360
|.网址	|1361
|.닷넷	|1362
|.コム	|1363
|.游戏	|1364
|.vermögensberater	|1365
|.vermögensberatung	|1366
|.企业	|1367
|.信息	|1368
|.嘉里大酒店	|1369
|.广东	|1372
|.இலங்கை	|1373
|.இந்தியா	|1374
|.հայ	|1375
|.新加坡	|1376
|.テスト	|1378
|.政务	|1379
|.xperia	|1380
|.yahoo	|1381
|.yamaxun	|1382
|.ye	|1383
|.you	|1384
|.yt	|1385
|.yun	|1386
|.za	|1387
|.zara	|1388
|.zero	|1389
|.zm	|1390
|.zw	|1391
|.xn--p1acf	|1392
|.xn--mgbt3dhd	|1393
|.able	|1394
|.aetna	|1395
|.arab	|1396
|.art	|1397
|.banamex	|1398
|.basketball	|1399
|.beauty	|1400
|.bestbuy	|1401
|.blog	|1402
|.booking	|1403
|.cam	|1404
|.capitalone	|1405
|.cbs	|1406
|.charity	|1407
|.chintai	|1408
|.citi	|1409
|.cookingchannel	|1410
|.dhl	|1411
|.diy	|1412
|.doctor	|1413
|.etisalat	|1414
|.farmers	|1415
|.food	|1416
|.foodnetwork	|1417
|.frontdoor	|1418
|.fujitsu	|1419
|.fun	|1420
|.games	|1421
|.gay	|1422
|.godaddy	|1423
|.hair	|1424
|.hdfc	|1425
|.hgtv	|1426
|.hisamitsu	|1427
|.hospital	|1428
|.hotels	|1429
|.ieee	|1430
|.intuit	|1431
|.jio	|1432
|.kosher	|1433
|.llc	|1434
|.llp	|1435
|.loft	|1436
|.map	|1437
|.mattel	|1438
|.mint	|1439
|.mitsubishi	|1440
|.monster	|1441
|.nfl	|1442
|.panasonic	|1443
|.pccw	|1444
|.pfizer	|1445
|.phd	|1446
|.pioneer	|1447
|.pramerica	|1448
|.pru	|1449
|.prudential	|1450
|.reliance	|1451
|.richardli	|1452
|.ril	|1453
|.rugby	|1454
|.search	|1455
|.ses	|1456
|.shopping	|1457
|.showtime	|1458
|.smart	|1459
|.swiftcover	|1460
|.tdk	|1461
|.travelchannel	|1462
|.xn--55qw42g	|1463
|.xn--5tzm5g	|1464
|.xn--8y0a063a	|1465
|.xn--fzys8d69uvgm	|1466
|.xn--kpu716f	|1467
|.xn--mgbaakc7dvf	|1468
|.xn--ngbrx	|1469
|.xn--pbt977c	|1470
|.xn--zfr164b	|1471
|.abarth	|1472
|.abc	|1473
|.airbus	|1474
|.alfaromeo	|1475
|.americanexpress	|1476
|.amex	|1477
|.anz	|1478
|.aol	|1479
|.auspost	|1480
|.bbt	|1481
|.blockbuster	|1482
|.bofa	|1483
|.case	|1484
|.caseih	|1485
|.cbre	|1486
|.comcast	|1487
|.cruise	|1488
|.data	|1489
|.dish	|1490
|.dot	|1491
|.dtv	|1492
|.dunlop	|1493
|.dvr	|1494
|.ericsson	|1495
|.esurance	|1496
|.fedex	|1497
|.ferrari	|1498
|.fiat	|1499
|.fidelity	|1500
|.fido	|1501
|.goodyear	|1502
|.hughes	|1503
|.itv	|1504
|.iveco	|1505
|.jeep	|1506
|.juniper	|1507
|.lancia	|1508
|.latino	|1509
|.lefrak	|1510
|.lego	|1511
|.lilly	|1512
|.locker	|1513
|.lundbeck	|1514
|.maserati	|1515
|.mckinsey	|1516
|.metlife	|1517
|.mobile	|1518
|.nab	|1519
|.nationwide	|1520
|.nba	|1521
|.newholland	|1522
|.ollo	|1523
|.onyourside	|1524
|.open	|1525
|.ott	|1526
|.phone	|1527
|.pnc	|1528
|.rmit	|1529
|.rogers	|1530
|.shangrila	|1531
|.sling	|1532
|.target	|1533
|.tiaa	|1534
|.ubank	|1535
|.ups	|1536
|.vanguard	|1537
|.visa	|1538
|.volvo	|1539
|.woodside	|1540
|.xfinity	|1541
|.xn--5su34j936bgsg	|1542
|.xn--otu796d	|1543
|.xn--w4rs40l	|1544
|.dupont	|1545
|.shop	|1546
|.audible	|1547
|.deal	|1548
|.eco	|1549
|.fire	|1550
|.free	|1551
|.hot	|1552
|.imdb	|1553
|.kindle	|1554
|.macys	|1555
|.merckmsd	|1556
|.msd	|1557
|.now	|1558
|.observer	|1559
|.pay	|1560
|.politie	|1561
|.prime	|1562
|.save	|1563
|.secure	|1564
|.silk	|1565
|.staples	|1566
|.wow	|1567
|.xn--1ck2e1b	|1568
|.xn--bck1b9a5dre4c	|1569
|.xn--cck2b3b	|1570
|.xn--eckvdtc9d	|1571
|.xn--fct429k	|1572
|.xn--gckr3f0f	|1573
|.xn--gk3at1e	|1574
|.xn--jlq61u9w7b	1575
|.xn--jvr189m	|1576
|.xn--rovu88b	|1577
|.zappos	|1578
|.hbo	|1579
|.xn--3ds443g	|1580
|.xn--d1acj3b	|1581
|.xn--fiq228c5hs	|1582
|.catholic	|1583
|.cpa	|1584
|.netflix	|1585
|.xn--80aqecdr1a	|1586
|.xn--mgba7c0bbn0a	|1587
|.xn--mgbca7dzdo	|1588
|.xn--mgbi4ecexp	|1589
|.xn--tiq49xqyj	|1590
|.boston	|1591
|.xn--ses554g	|1592
|.nike	|1593
|.allstate	|1594
|.hyatt	|1595
|.afamilycompany	|1596
|.americanfamily	|1597
|.amfam	|1598
|.asda	|1599
|.athleta	|1600
|.bananarepublic	|1601
|.baseball	|1602
|.calvinklein	|1603
|.duck	|1604
|.fujixerox	|1605
|.gap	|1606
|.george	|1607
|.glade	|1608
|.grocery	|1609
|.guardian	|1610
|.homegoods	|1611
|.homesense	|1612
|.marshalls	|1613
|.mit	|1614
|.mlb	|1615
|.off	|1616
|.oldnavy	|1617
|.raid	|1618
|.rightathome	|1619
|.samsclub	|1620
|.scjohnson	|1621
|.tjmaxx	|1622
|.tjx	|1623
|.tkmaxx	|1624
|.walmart	|1625
|.winners	|1626
|.africa	|1627
|.ikano	|1628
|.xn--3oq18vl8pn36a	|1629
|.	|1630
|.radio	|1631
|.realestate	|1632
|.xn--vuq861b	|1633
|.moto	|1634
|.lpl	|1635
|.lplfinancial	|1636
|.vivo	|1637
|.qvc	|1638
|.box	|1639
|.inc	|1640
|.sport	|1641
|.amazon	|1642
|.xn--cckwcxetd	|1643
|.xn--jlq480n2rg	|1644
|.flir	|1645

### Examples

Typical API call example: `https://domainlists.io/api/deleted/534/me@domainlists.io/MySecretPsw/`  
This returns a list of deleted .COM domains (534 is the code for .com zone, check the table above) using user account me@domainlists.io with password MySecretPsw.
