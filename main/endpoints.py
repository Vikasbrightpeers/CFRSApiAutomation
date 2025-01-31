# ----------------------url's and endpoints-------------------------------------------

dev_auth_url = 'https://cfs-auth-dev.tgstechnology.net/'
# dev_auth_url = 'https://cfs-auth-qa.tgstechnology.net/'
test_auth_url = 'https://test-cfrs-auth.tgstechnology.net/'
qa_auth_url = 'https://cfs-auth-qa.tgstechnology.net/'

dev_admin_url = 'https://cfs-admin-dev.tgstechnology.net/api/Admin/'
qa_admin_url = 'https://cfs-admin-qa.tgstechnology.net/api/Admin/'

dev_committee_url = 'https://cfs-committee-dev.tgstechnology.net/api/Committee/'
qa_committee_url = 'https://cfs-committee-qa.tgstechnology.net/api/Committee/'


# ----------------------- Auth -----------------------
dev_login_url = 'api/Auth/login'
dev_my_admin_role_list = 'api/Auth/AdminDashboard/getMyAdminRoleList'

dev_admin_notes_category = 'api/Auth/AdministrativeNotes/getAllAdminNotesCategory'
dev_administrative_data_list = 'api/Auth/AdministrativeNotes/getAdministrativeNoteDataList'
dev_add_administrative_notes = 'api/Auth/AdministrativeNotes/addAdministrativeNote'

save_security_question_info = 'api/Auth/saveSecurityQuestionInfo'
add_and_update_user = 'api/Auth/ManageUsers/addAndUpdateUser'

get_all_security_questions = 'api/Auth/getAllSecurityQuestions'
verify_user_question_and_answer = 'api/Auth/verifyUserQuestionAndAnswer'

forgot_username = 'api/Auth/forgotUsername'

get_website_configuration = 'api/Auth/AppConfigure/getWebsiteConfiguration'
get_app_page_configuration = 'api/Auth/AppConfigure/getAppPageConfig/'

# Committee User Profile
get_pending_committee_access_requests = 'api/Auth/CommitteeUserProfile/getPendingCommitteeAccessRequests'
update_committee_access_status = '/api/Auth/CommitteeUserProfile/updateCommitteeAccessStatus'

# Committee Users
get_my_committee_users_data_list = 'api/Auth/CommitteeUsers/getMyCommitteeUsersDataList'
get_my_committee_invite_users_data_list = 'api/Auth/CommitteeUsers/getMyCommitteeInviteUsersDataList'

# User Access
get_user_registration_count = 'api/Auth/UserAccess/getUseRegistrationCount'

# My Profile Messages
get_my_profile_notifications = 'api/Auth/MyProfileMessage/getMyProfileNotifications'

# My Profile
get_profile_details_by_userid = 'api/Auth/MyProfile/getProfileDetailsByUserId'
get_user_question_info = 'api/Auth/MyProfile/getUserQuestionInfo'
update_question_answer_info = 'api/Auth/MyProfile/updateUserQuestion'
update_user_profile = 'api/Auth/MyProfile/updateUserProfile'
update_profile_password = 'api/Auth/MyProfile/updateProfilePassword'

# Manage User
get_user_list = 'api/Auth/ManageUsers/getUserList'
get_user_profile_by_id = 'api/Auth/ManageUsers/getUserProfileById/'
force_user_to_change_on_next_login = 'api/Auth/ManageUsers/forceUserToChangeOnNextLogin'
create_system_generated_password = 'api/Auth/ManageUsers/createSystemGeneratedPassword'
create_new_password = 'api/Auth/ManageUsers/createNewPassword'
get_all_user_role = 'api/Auth/ManageUsers/getAllUserRole'
get_all_admin_role = 'api/Auth/ManageUsers/getAllAdminRole'
add_user_access = 'api/Auth/ManageUsers/addUserAccess'
update_user_access_status = 'api/Auth/ManageUsers/updateUserAccessStatus'
get_admin_role_by_user_data_list = 'api/Auth/ManageUsers/getAdminRoleByUserDataList'
get_user_role_by_user_data_list = 'api/Auth/ManageUsers/getUsersRoleByUserDataList'
get_user_committee_access_data_list = 'api/Auth/ManageUsers/getUsersCommitteeAccessDataList'

# My Committee
get_all_org_pending_registrations_data_list = 'api/Auth/ManageUsers/getAllOrgPendingRegistrationsDataList'
get_my_committee_list = "api/Auth/MyCommittee/getMyCommitteeList"
add_user_login_history = "api/Auth/MyCommittee/addUserOrgLoginHistory"
get_user_login_session_by_org_id = "api/Auth/MyCommittee/getUserLoginSessionsByOrgId"
get_user_reporting_activity_by_org_id = "api/Auth/MyCommittee/getUserReportingActivityByOrgId"

# transaction
transactionUrl = "CommitteeTransactions/addTransaction"
get_all_transactions = "CommitteeTransactions/getAllTransactionDataList"
update_transactions = 'CommitteeTransactions/updateTransaction'
delete_transactions = 'CommitteeTransactions/deleteTransactionById/'
return_transactions = 'CommitteeTransactions/addRetunTransaction'

# registration
post_registration = 'CommitteeRegistration/submitCommitteeRegistrationData'
get_all_committee_registrations = 'CommitteeRegistration/getAllCommitteeRegistrationDataList'

# Notification
notificationUrl = dev_admin_url + '/Notification/'
