-- 创建数据库
CREATE DATABASE IF NOT EXISTS graduate_info CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE graduate_info;

-- 创建学校信息表
CREATE TABLE `school` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school_name` varchar(100) NOT NULL COMMENT '学校名称',
  `logo_url` varchar(255) NOT NULL COMMENT '学校logo地址',
  `tag` varchar(100) DEFAULT NULL COMMENT '学校标签，如"双一流"建设高校',
  `self_evaluation` tinyint(1) DEFAULT '0' COMMENT '是否自划线院校',
  `notice` varchar(255) NOT NULL COMMENT '网报公告链接',
  `enrollment_guide` varchar(255) NOT NULL COMMENT '招生简章链接',
  `online_consult_url` varchar(255) NOT NULL COMMENT '在线咨询链接',
  `adjustment_method` varchar(255) NOT NULL COMMENT '调剂办法链接',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uni_name` (`school_name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 COMMENT='学校信息表';

-- 创建专业信息表
CREATE TABLE IF NOT EXISTS enrollment_plan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    school_id INT NOT NULL COMMENT '学校ID',
    school_name VARCHAR(100) NOT NULL COMMENT '学校名称',
    name VARCHAR(100) NOT NULL COMMENT '专业名称',
    code VARCHAR(20) NOT NULL COMMENT '专业代码',
    total_quota INT  NOT NULL COMMENT '总招生人数',
    full_time_quota INT  COMMENT '全日制招生人数',
    part_time_quota INT  COMMENT '非全日制招生人数',
    year INT  COMMENT '年份',
    department VARCHAR(100) COMMENT '所属院系',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY uk_year_school_code_major_code (school_id, code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='专业信息表';

-- 创建分数线表
CREATE TABLE IF NOT EXISTS score_lines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    major_id INT NOT NULL COMMENT '专业ID',
    year INT NOT NULL COMMENT '年份',
    score_type TINYINT NOT NULL COMMENT '分数类型：1-专业课，2-公共课',
    score DECIMAL(5,2) NOT NULL COMMENT '分数',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (major_id) REFERENCES majors(id),
    UNIQUE KEY uk_major_year_type (major_id, year, score_type)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='分数线表';

-- 创建调剂信息表
CREATE TABLE IF NOT EXISTS adjustments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    major_id INT NOT NULL COMMENT '专业ID',
    content TEXT NOT NULL COMMENT '调剂信息内容',
    pub_date DATE NOT NULL COMMENT '发布日期',
    source_url VARCHAR(255) COMMENT '信息来源链接',
    status TINYINT DEFAULT 1 COMMENT '状态：1-有效，0-无效',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (major_id) REFERENCES majors(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='调剂信息表';