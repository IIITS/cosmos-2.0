beautify_digit = dict()
beautify_digit["1"]="001"
beautify_digit["2"]="002"
beautify_digit["3"]="003"
beautify_digit["4"]="004"
beautify_digit["5"]="005"
beautify_digit["6"]="006"
beautify_digit["7"]="007"
beautify_digit["8"]="008"
beautify_digit["9"]="009"
beautify_digit["10"]="010"
beautify_digit["11"]="011"
beautify_digit["12"]="012"
beautify_digit["13"]="013"
beautify_digit["14"]="014"
beautify_digit["15"]="015"
beautify_digit["16"]="016"
beautify_digit["17"]="017"
beautify_digit["18"]="018"
beautify_digit["19"]="019"
#---------------------------#
# URL configurations are 	#
# defined below:			#
#---------------------------#

url_ref = {'index':{},'gp':{}, 'btp':{},'feasta':{}, 'accounts':{}}
url_ref['index']['index']="/"
# URL References for Accounts 
url_ref['accounts']['login']="/accounts/login/"
url_ref['accounts']['password_change']="/secure/changepassword/"
url_ref['accounts']['password_change_success']="/password-changed/"
url_ref['accounts']['signout']="/accounts/signout/"

# URL References for Application: BTP and Honors
url_ref['btp']['index'] = "/btp/"
url_ref['btp']['add_project'] = "/btp/add-project/"
url_ref['btp']['post_report'] = "/btp/post/report/"
url_ref['btp']['edit_project'] = "/btp/edit-project/"
url_ref['btp']['edit_submit_project'] = "/btp/edit-submit-project/"
url_ref['btp']['submit_project'] = "/btp/submit-project/"
url_ref['btp']['add_students'] = "/btp/add-students/"
url_ref['btp']['get_current_students'] = "/btp/get-current-students/"
url_ref['btp']['upload_project_file'] = "/btp/upload-project-file"
url_ref['btp']['file_delete'] = "/btp/file-delete"
url_ref['btp']['move_to_archives'] = "/btp/move-to-archives/"
url_ref['btp']['archive_restore'] = "/btp/archive-restore/"

# URL References for Application: Issues and Suggestions

# URL Reference for Application: Feasta

#---------------------------#
# Template configurations	# 
# are defined below:		#
#---------------------------#
template_ref = {'gp':{}, 'btp':{}, 'feasta':{}}

template_ref['btp']['index'] = "/btp/"
template_ref['btp']['add_project'] = "/btp/"
template_ref['btp']['post_report'] = "/btp/"
template_ref['btp']['edit_project'] = "/btp/"
template_ref['btp']['edit_submit_project'] = "/btp/"
template_ref['btp']['add_students'] = "/btp/"
template_ref['btp']['get_current_students'] = "/btp/"
template_ref['btp']['upload_project_file'] = "/btp/"
template_ref['btp']['file_delete'] = "/btp/"
template_ref['btp']['move_to_archives'] = "/btp/"
template_ref['btp']['archive_restore'] = "/btp/"