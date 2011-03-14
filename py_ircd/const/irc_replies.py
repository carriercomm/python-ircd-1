# -*- coding: utf-8 -*-

# Dizionario generato automaticamente tramite un parser dall'RFC ufficiale
# associa a chiave RPL_something il valore di una tupla formata da ( 'valore numerico', 'funzione per la stampa del messaggio' )
#
# Esempio di utilsizzo:
#
#	print 'RPL_WELCOME:', dict['RPL_WELCOME'][1]('provanick!provauser@provahost')
#	stamperà:
#	"RPL_WELCOME: Welcome to the Internet Relay Network provanick!provauser@provahost"
#	comunque viene utilizzato solo tramite Client.reply

dict = {
	'RPL_WELCOME' : ('001', lambda ident: "Welcome to the Internet Relay Network %s" % (ident)),
	'RPL_YOURHOST' : ('002', lambda servername, ver: "Your host is %s, running version %s" % (servername, ver)),
	'RPL_CREATED' : ('003', lambda date: "This server was created %s" % (date)),
	'RPL_MYINFO' : ('004', lambda servername, version, available_user_modes, available_channel_modes: "%s %s %s %s"  % (servername, version, available_user_modes, available_channel_modes)),
	'RPL_BOUNCE' : ('005', lambda server_name, port_number: "Try server %s, port %s"  % (server_name, port_number)),
	
	'RPL_USERHOST' : ('302', lambda reply: ":*1%s *( " " %s )" % (reply, reply)),
	'RPL_ISON' : ('303', lambda nick: ":*1%s *( " " %s )"  % (nick, nick)),
	'RPL_AWAY' : ('301', lambda nick, away_message: "%s :%s" % (nick, away_message)),
	'RPL_UNAWAY' : ('305', lambda : ":You are no longer marked as being away" % ()),
	'RPL_NOWAWAY' : ('306', lambda : ":You have been marked as being away"  % ()),
	'RPL_WHOISUSER' : ('311', lambda nick, user, host, real_name: "%s %s %s * :%s" % (nick, user, host, real_name)),
	'RPL_WHOISSERVER' : ('312', lambda nick, server, server_info: "%s %s :%s" % (nick, server, server_info)),
	'RPL_WHOISOPERATOR' : ('313', lambda nick: "%s :is an IRC operator" % (nick)),
	'RPL_WHOISIDLE' : ('317', lambda nick, integer: "%s %s :seconds idle" % (nick, integer)),
	'RPL_ENDOFWHOIS' : ('318', lambda nick: "%s :End of WHOIS list" % (nick)),
	'RPL_WHOISCHANNELS' : ('319', lambda nick, channel: """%s :*( ( "@" / "\+" ) %s " " )"""  % (nick, channel)),
	'RPL_WHOWASUSER' : ('314', lambda nick, user, host, real_name: "%s %s %s * :%s" % (nick, user, host, real_name)),
	'RPL_ENDOFWHOWAS' : ('369', lambda nick: "%s :End of WHOWAS"  % (nick)),
	'RPL_LIST' : ('322', lambda channel, visible, topic: "%s %s :%s" % (channel, visible, topic)),
	'RPL_LISTEND' : ('323', lambda : ":End of LIST"  % ()),
	'RPL_UNIQOPIS' : ('325', lambda channel, nickname: "%s %s" % (channel, nickname)),
	'RPL_CHANNELMODEIS' : ('324', lambda channel, mode, mode_params: "%s %s %s" % (channel, mode, mode_params)),
	'RPL_NOTOPIC' : ('331', lambda channel: "%s :No topic is set" % (channel)),
	'RPL_TOPIC' : ('332', lambda channel, topic: "%s :%s"  % (channel, topic)),
	'RPL_INVITING' : ('341', lambda channel, nick: "%s %s"  % (channel, nick)),
	'RPL_SUMMONING' : ('342', lambda user: "%s :Summoning user to IRC"  % (user)),
	'RPL_INVITELIST' : ('346', lambda channel, invitemask: "%s %s" % (channel, invitemask)),
	'RPL_ENDOFINVITELIST' : ('347', lambda channel: "%s :End of channel invite list"  % (channel)),
	'RPL_EXCEPTLIST' : ('348', lambda channel, exceptionmask: "%s %s" % (channel, exceptionmask)),
	'RPL_ENDOFEXCEPTLIST' : ('349', lambda channel: "%s :End of channel exception list"  % (channel)),
	'RPL_VERSION' : ('351', lambda version, debuglevel, server, comments: "%s.%s %s :%s" % (version, debuglevel, server, comments)),
	'RPL_WHOREPLY' : ('352', lambda channel, user, host, server, nick, hopcount, real_name: """%s %s %s %s %s ( "H" / "G" > ["*"] [ ( "@" / "+" ) ] :%s %s""" % (channel, user, host, server, nick, hopcount, real_name)),
	'RPL_ENDOFWHO' : ('315', lambda name: "%s :End of WHO list"  % (name)),
	'RPL_NAMREPLY' : ('353', lambda scope_flag, channel, nicklist: "%s %s :%s" % (scope_flag, channel, nicklist)),
	'RPL_ENDOFNAMES' : ('366', lambda channel: "%s :End of NAMES list"  % (channel)),
	'RPL_LINKS' : ('364', lambda mask, server, hopcount, server_info: "%s %s :%s %s" % (mask, server, hopcount, server_info)),
	'RPL_ENDOFLINKS' : ('365', lambda mask: "%s :End of LINKS list"  % (mask)),
	'RPL_BANLIST' : ('367', lambda channel, banmask: "%s %s" % (channel, banmask)),
	'RPL_ENDOFBANLIST' : ('368', lambda channel: "%s :End of channel ban list"  % (channel)),
	'RPL_INFO' : ('371', lambda string: ":%s" % (string)),
	'RPL_ENDOFINFO' : ('374', lambda : ":End of INFO list"  % ()),
	'RPL_MOTDSTART' : ('375', lambda : ":" % ()),
	'RPL_MOTD' : ('372', lambda text: ":%s" % (text)),
	'RPL_ENDOFMOTD' : ('376', lambda : ":End of MOTD command"  % ()),
	'RPL_YOUREOPER' : ('381', lambda : ":You are now an IRC operator"  % ()),
	'RPL_REHASHING' : ('382', lambda config_file: "%s :Rehashing"  % (config_file)),
	'RPL_YOURESERVICE' : ('383', lambda servicename: "You are service %s"  % (servicename)),
	'RPL_TIME' : ('391', lambda server, string_showing_servers_local_time: "%s :%s"  % (server, string_showing_servers_local_time)),
	'RPL_USERSSTART' : ('392', lambda : ":UserID Terminal Host" % ()),
	'RPL_USERS' : ('393', lambda username, ttyline, hostname: ":%s %s %s" % (username, ttyline, hostname)),
	'RPL_ENDOFUSERS' : ('394', lambda : ":End of users" % ()),
	'RPL_NOUSERS' : ('395', lambda : ":Nobody logged in"  % ()),
	'RPL_TRACELINK' : ('200', lambda version_debug_level, destination, next_server, protocol_version, link_uptime_in_seconds, backstream_sendq, upstream_sendq: "Link %s %s %s V%s %s %s %s" % (version_debug_level, destination, next_server, protocol_version, link_uptime_in_seconds, backstream_sendq, upstream_sendq)),
	'RPL_TRACECONNECTING' : ('201', lambda _class, server: "Try. %s %s" % (_class, server)),
	'RPL_TRACEHANDSHAKE' : ('202', lambda _class, server: "H.S. %s %s" % (_class, server)),
	'RPL_TRACEUNKNOWN' : ('203', lambda _class, client_ip_address_in_dot_form: "???? %s [%s]" % (_class, client_ip_address_in_dot_form)),
	'RPL_TRACEOPERATOR' : ('204', lambda _class, nick: "Oper %s %s" % (_class, nick)),
	'RPL_TRACEUSER' : ('205', lambda _class, nick: "User %s %s" % (_class, nick)),
	'RPL_TRACESERVER' : ('206', lambda _class, int, server, nickuser, hostserver, protocol_version: "Serv %s %sS %sC %s %s@%s V%s" % (_class, int, int, server, nickuser, hostserver, protocol_version)),
	'RPL_TRACESERVICE' : ('207', lambda _class, name, type, active_type: "Service %s %s %s %s" % (_class, name, type, active_type)),
	'RPL_TRACENEWTYPE' : ('208', lambda newtype, client_name: "%s 0 %s" % (newtype, client_name)),
	'RPL_TRACE_class' : ('209', lambda _class, count: "_class %s %s" % (_class, count)),
	'RPL_TRACELOG' : ('261', lambda logfile, debug_level: "File %s %s" % (logfile, debug_level)),
	'RPL_TRACEEND' : ('262', lambda server_name, version_debug_level: "%s %s :End of TRACE"  % (server_name, version_debug_level)),
	'RPL_STATSLINKINFO' : ('211', lambda linkname, sendq, sent_messages, sent_kbytes, received_messages, received_kbytes, time_open: "%s %s %s %s %s %s %s"  % (linkname, sendq, sent_messages, sent_kbytes, received_messages, received_kbytes, time_open)),
	'RPL_STATSCOMMANDS' : ('212', lambda command, count, byte_count, remote_count: "%s %s %s %s"  % (command, count, byte_count, remote_count)),
	'RPL_ENDOFSTATS' : ('219', lambda stats_letter: "%s :End of STATS report" % (stats_letter)),
	'RPL_STATSUPTIME' : ('242', lambda : ":Server Up %d days %d:%02d:%02d"  % ()),
	'RPL_STATSOLINE' : ('243', lambda hostmask, name: "O %s * %s"  % (hostmask, name)),
	'RPL_UMODEIS' : ('221', lambda user_mode_string: "%s"  % (user_mode_string)),
	'RPL_SERVLIST' : ('234', lambda name, server, mask, type, hopcount, info: "%s %s %s %s %s %s" % (name, server, mask, type, hopcount, info)),
	'RPL_SERVLISTEND' : ('235', lambda mask, type: "%s %s :End of service listing"  % (mask, type)),
	'RPL_LUSERCLIENT' : ('251', lambda integer: ":There are %s users and %s services on %s servers" % (integer, integer, integer)),
	'RPL_LUSEROP' : ('252', lambda integer: "%s :operator(s) online" % (integer)),
	'RPL_LUSERUNKNOWN' : ('253', lambda integer: "%s :unknown connection(s)" % (integer)),
	'RPL_LUSERCHANNELS' : ('254', lambda integer: "%s :channels formed" % (integer)),
	'RPL_LUSERME' : ('255', lambda integer: ":I have %s clients and %s servers"  % (integer, integer)),
	'RPL_ADMINME' : ('256', lambda server: "%s :Administrative info" % (server)),
	'RPL_ADMINLOC1' : ('257', lambda admin_info: ":%s" % (admin_info)),
	'RPL_ADMINLOC2' : ('258', lambda admin_info: ":%s" % (admin_info)),
	'RPL_ADMINEMAIL' : ('259', lambda admin_info: ":%s"  % (admin_info)),
	'RPL_TRYAGAIN' : ('263', lambda command: "%s :Please wait a while and try again."  % (command)),
	
	'ERR_NOSUCHNICK' : ('401', lambda nickname: "%s :No such nick/channel"  % (nickname)),
	'ERR_NOSUCHSERVER' : ('402', lambda server_name: "%s :No such server"  % (server_name)),
	'ERR_NOSUCHCHANNEL' : ('403', lambda channel_name: "%s :No such channel"  % (channel_name)),
	'ERR_CANNOTSENDTOCHAN' : ('404', lambda channel_name: "%s :Cannot send to channel"  % (channel_name)),
	'ERR_TOOMANYCHANNELS' : ('405', lambda channel_name: "%s :You have joined too many channels"  % (channel_name)),
	'ERR_WASNOSUCHNICK' : ('406', lambda nickname: "%s :There was no such nickname"  % (nickname)),
	'ERR_TOOMANYTARGETS' : ('407', lambda target, error_code, abort_message: "%s :%s recipients. %s"  % (target, error_code, abort_message)),
	'ERR_NOSUCHSERVICE' : ('408', lambda service_name: "%s :No such service"  % (service_name)),
	'ERR_NOORIGIN' : ('409', lambda : ":No origin specified"  % ()),
	'ERR_NORECIPIENT' : ('411', lambda command: ":No recipient given (%s)" % (command)),
	'ERR_NOTEXTTOSEND' : ('412', lambda : ":No text to send" % ()),
	'ERR_NOTOPLEVEL' : ('413', lambda mask: "%s :No toplevel domain specified" % (mask)),
	'ERR_WILDTOPLEVEL' : ('414', lambda mask: "%s :Wildcard in toplevel domain" % (mask)),
	'ERR_BADMASK' : ('415', lambda mask, server, host: "%s :Bad Server/host mask" % (mask, server, host)),
	'ERR_UNKNOWNCOMMAND' : ('421', lambda command: "%s :Unknown command"  % (command)),
	'ERR_NOMOTD' : ('422', lambda : ":MOTD File is missing"  % ()),
	'ERR_NOADMININFO' : ('423', lambda server: "%s :No administrative info available"  % (server)),
	'ERR_FILEERROR' : ('424', lambda file_op, file: ":File error doing %s on %s"  % (file_op, file)),
	'ERR_NONICKNAMEGIVEN' : ('431', lambda : ":No nickname given"  % ()),
	'ERR_ERRONEUSNICKNAME' : ('432', lambda nick: "%s :Erroneous nickname"  % (nick)),
	'ERR_NICKNAMEINUSE' : ('433', lambda nick: "%s :Nickname is already in use"  % (nick)),
	'ERR_NICKCOLLISION' : ('436', lambda nick, user, host: "%s :Nickname collision KILL from %s@%s"  % (nick, user, host)),
	'ERR_UNAVAILRESOURCE' : ('437', lambda nickchannel: "%s :Nick/channel is temporarily unavailable"  % (nickchannel)),
	'ERR_USERNOTINCHANNEL' : ('441', lambda nick, channel: "%s %s :They aren't on that channel"  % (nick, channel)),
	'ERR_NOTONCHANNEL' : ('442', lambda channel: "%s :You're not on that channel"  % (channel)),
	'ERR_USERONCHANNEL' : ('443', lambda user, channel: "%s %s :is already on channel"  % (user, channel)),
	'ERR_NOLOGIN' : ('444', lambda user: "%s :User not logged in"  % (user)),
	'ERR_SUMMONDISABLED' : ('445', lambda : ":SUMMON has been disabled"  % ()),
	'ERR_USERSDISABLED' : ('446', lambda : ":USERS has been disabled"  % ()),
	'ERR_NOTREGISTERED' : ('451', lambda : ":You have not registered"  % ()),
	'ERR_NEEDMOREPARAMS' : ('461', lambda command: "%s :Not enough parameters"  % (command)),
	'ERR_ALREADYREGISTRED' : ('462', lambda : ":Unauthorized command (already registered)"  % ()),
	'ERR_NOPERMFORHOST' : ('463', lambda : ":Your host isn't among the privileged"  % ()),
	'ERR_PASSWDMISMATCH' : ('464', lambda : ":Password incorrect"  % ()),
	'ERR_YOUREBANNEDCREEP' : ('465', lambda : ":You are banned from this server"  % ()),
	'ERR_KEYSET' : ('467', lambda channel: "%s :Channel key already set" % (channel)),
	'ERR_CHANNELISFULL' : ('471', lambda channel: "%s :Cannot join channel (+l)" % (channel)),
	'ERR_UNKNOWNMODE' : ('472', lambda char, channel: "%s :is unknown mode char to me for %s" % (char, channel)),
	'ERR_INVITEONLYCHAN' : ('473', lambda channel: "%s :Cannot join channel (+i)" % (channel)),
	'ERR_BANNEDFROMCHAN' : ('474', lambda channel: "%s :Cannot join channel (+b)" % (channel)),
	'ERR_BADCHANNELKEY' : ('475', lambda channel: "%s :Cannot join channel (+k)" % (channel)),
	'ERR_BADCHANMASK' : ('476', lambda channel: "%s :Bad Channel Mask" % (channel)),
	'ERR_NOCHANMODES' : ('477', lambda channel: "%s :Channel doesn't support modes" % (channel)),
	'ERR_BANLISTFULL' : ('478', lambda channel, char: "%s %s :Channel list is full" % (channel, char)),
	'ERR_NOPRIVILEGES' : ('481', lambda : ":Permission Denied" % ()),
	'ERR_CHANOPRIVSNEEDED' : ('482', lambda channel: "%s :You're not channel operator"  % (channel)),
	'ERR_CANTKILLSERVER' : ('483', lambda : ":You can't kill a server!"  % ()),
	'ERR_RESTRICTED' : ('484', lambda : ":Your connection is restricted!" % ()),
	'ERR_UNIQOPPRIVSNEEDED' : ('485', lambda : ":You're not the original channel operator" % ()),
	'ERR_NOOPERHOST' : ('491', lambda : ":No O-lines for your host" % ()),
	'ERR_UMODEUNKNOWNFLAG' : ('501', lambda : ":Unknown MODE flag"  % ()),
	'ERR_USERSDONTMATCH' : ('502', lambda : ":Cannot change mode for other users"  % ())
}