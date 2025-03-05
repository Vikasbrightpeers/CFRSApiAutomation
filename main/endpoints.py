# ---------------------- url's and endpoints-------------------------------------------

dev_auth_url = 'https://cfs-auth-dev.tgstechnology.net/'
# dev_auth_url = 'https://cfs-auth-qa.tgstechnology.net/'
test_auth_url = 'https://test-cfrs-auth.tgstechnology.net/'
qa_auth_url = 'https://cfs-auth-qa.tgstechnology.net/'

dev_admin_url = 'https://cfs-admin-dev.tgstechnology.net/api/Admin/'
# dev_admin_url = 'https://test-cfrs-admin.tgstechnology.net/api/Admin/'

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
get_committee_profile_by_org_id = 'CommitteeRegistration/getCommitteeProfileByOrgId/'
get_all_officer_information_by_org_id = 'CommitteeRegistration/getAllOfficersInformationByOrgId/'
edit_pending_org_registration_status = 'CommitteeRegistration/editPendingOrgRegistrationStatus/'
get_all_org_reasons_by_status_code = 'CommitteeRegistration/getAllOrgReasonsByStatusCode/'
view_org_registration_report = 'CommitteeRegistration/viewOrgRegistrationReport/'

# Admin
# Notifications
get_all_notifications_type = 'Notification/getAllNotificationType'
get_all_notification_view_status = 'Notification/getAllNotificationViewStatus'
get_all_notifications_data_list = 'Notification/getAllAdminNotificationDataList'
add_edit_notification = 'Notification/addEditNotification'
delete_notification = 'Notification/deleteNotificationById/'
get_notification_by_Id = 'Notification/getNotificationDetailsById/'
get_all_notification_for_badges = 'Notification/getAllAdminNotificationForBadges'
get_all_admin_notification = 'Notification/getAllAdminNotification'

# Committee Summary
get_org_details_for_correct_registration_by_org_id = 'CommitteeSummary/getOrgDetailsForCorrectRegistrationByOrgID/'
submit_correct_registration = 'CommitteeSummary/submitCorrectOrgRegistration/'

# Committee Transactions Chart
get_contribution_chart_data = 'CommitteeTransactions/getContributionChartData'
get_expenditure_chart_data = 'CommitteeTransactions/getExpenditureChartData'

# correspondence
get_org_info_for_correspondence_data_list = 'Correspondence/getOrgInfoForCorrespondenceDataList'
get_correspondence_data_list = 'Correspondence/getCorrespondenceDataList'
add_correspondence = 'Correspondence/addCorrespondence'

# Committee Report
get_org_filed_report_data_list = 'CommitteeReport/getOrgFiledReportDataList'
get_org_filed_report_amend_history = 'CommitteeReport/getOrgFiledReportAmendHistory/'

# Committee Document
get_all_org_documents_data_list = 'CommitteeDocuments/getAllOrgDocumentsDataList'
get_org_documents_by_document_id = 'CommitteeDocuments/getOrgDocumentByDocumentID/'
delete_org_document = 'CommitteeDocuments/deleteOrgDocument'


# Admin report
admin_sub_report_type = 'AdminReport/GetAdminSubReportType/'
generate_administration_report = 'AdminReport/generateAdministrationReport/'

# Audit Review

get_all_transaction_for_audit_review_data_list = 'AuditReview/getAllTransactionForAuditReviewDataList'
get_all_report_for_audit_review_data_list = 'AuditReview/getAllReportForAuditReviewDataList'
get_all_committee_for_audit_review_data_list = 'AuditReview/getAllCommitteeForAuditReviewDataList'
get_compliance_information_by_org_compliance_id = 'AuditReview/getComplianceInformationByOrgComplianceId/'

get_violation_by_id = 'AuditReview/getViolationById/'
add_edit_violation = 'AuditReview/addEditViolation/'

add_edit_violation_payment = 'AuditReview/addEditViolationPayment/'
get_violation_payment_by_id = 'AuditReview/getViolationPaymentById/'
get_all_violation_payment_data_list = 'AuditReview/getAllViolationPaymentDataList/'
delete_violation_payment = 'AuditReview/deleteViolationPayment/'

update_compliance_status = 'AuditReview/updateComplianceStatus/'

add_edit_violation_waiver = 'AuditReview/addEditViolationWaiver/'
get_violation_waiver_by_id = 'AuditReview/getViolationWaiverById/'
get_all_violation_waiver_data_list = 'AuditReview/getAllViolationWaiverDataList/'
delete_violation_waiver = 'AuditReview/deleteViolationWaiverById/'

# Reporting Schedule
# Election
add_edit_election = 'ReportingSchedule/addEditElection'
get_election_by_id = 'ReportingSchedule/getElectionById/'
delete_election_by_id = 'ReportingSchedule/DeleteElectionById/'
get_all_election_data_list = 'ReportingSchedule/getAllElectionDataList'

# Reporting Cycle
add_edit_reporting_cycle = 'ReportingSchedule/addEditReportingCycle'
get_reporting_cycle_by_id = 'ReportingSchedule/getReportingCycleById/'
delete_reporting_cycle_by_id = 'ReportingSchedule/DeleteReportingCycleById/'
get_all_reporting_cycle_data_list = 'ReportingSchedule/getAllReportingCycleDataList'


# Reporting Period
add_edit_reporting_period = 'ReportingSchedule/addEditRepotingPeriod'
get_reporting_period_by_id = 'ReportingSchedule/getReportingPeriodById/'
delete_reporting_period_by_id = 'ReportingSchedule/DeleteReportingPeriodById/'
get_all_reporting_period_data_list = 'ReportingSchedule/getAllReportingPeriodDataList'
