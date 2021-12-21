CREATE TABLE `bdrs_one` (
  `id` varchar(50) NOT NULL,
  `shun_xu` int(50) DEFAULT NULL,
  `biao_ti` varchar(1024) DEFAULT NULL,
  `tu_pian` varchar(1024) DEFAULT NULL,
  `miao_shu` varchar(1024) DEFAULT NULL,
  `reshou_zhishu` int(11) DEFAULT NULL,
  `insert_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `rs_shijian` varchar(50) DEFAULT NULL COMMENT '热搜时间',
  KEY `biao_ti` (`biao_ti`),
  KEY `rs_shijian` (`rs_shijian`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;