/*
 * $Id$
 *
 * Generic uqwk config
 */

#define CONFIGNAME	"pld"

#define DEF_BBS_NAME	"The BBS That Shall Not Be Named"
#define DEF_BBS_CITY	"Nowhere, Utopia"
#define DEF_BBS_PHONE	"555-1212"
#define DEF_BBS_SYSOP	"Joe A. Sysop"
#define DEF_BBS_ID	"0,TBSNBN-BBS"

#ifndef NNTP
  #define DEF_ACT_FILE	"/var/lib/news/active"
  #define DEF_NEWS_DIR	"/var/spool/news"
#endif
#define	DEF_MAIL_DIR	"/var/mail"

#define SENDMAIL	"/usr/lib/sendmail -i"
#define INEWS_PATH      "/usr/bin/inews"
#define NNTP_HOST_FILE  "/var/lib/news/nntp_server"	/* news server file */
