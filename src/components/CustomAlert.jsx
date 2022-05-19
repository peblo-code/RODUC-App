import { View } from 'react-native'
import ModalStyled from './ModalStyled.jsx'
import StyledText from './StyledText.jsx'

const CustomAlert = ({ isShowed, title, message, children }) => {
    return (
        <View>
            <ModalStyled isVisible={ isShowed }>
                <View style={{marginBottom: 20}}>
                    <StyledText
                        align='center'
                        color='primary'
                        fontSize='large'>{ title }
                    </StyledText>

                    <StyledText
                        align='center'
                        color='secondary'
                        fontSize='subheading'
                        style={{ marginTop: 10 }}> { message }
                    </StyledText>
                </View>

                { children }

            </ModalStyled>
        </View>
    )
}

export default CustomAlert